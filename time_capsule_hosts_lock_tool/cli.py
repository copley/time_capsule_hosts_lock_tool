#!/usr/bin/env python3
import argparse
import sys
import os
import datetime
from getpass import getpass

from . import lock_control, password_storage, scheduler, config, utils

def check_root():
    if os.geteuid() != 0:
        print("This utility must be run as root. Exiting.")
        sys.exit(1)

def lock():
    # Check if already locked
    state = config.load_state()
    if state and state.get("is_locked"):
        print("The hosts file is already locked until {}.".format(state.get("lock_until")))
        return

    print("Locking /etc/hosts...")
    # Prompt for password (twice)
    password = getpass("Enter lock password: ")
    password_confirm = getpass("Confirm lock password: ")
    if password != password_confirm:
        print("Passwords do not match. Exiting.")
        sys.exit(1)

    # Prompt for duration
    duration_str = input("Enter lock duration (e.g., 2h, 120m, 1d): ")
    try:
        duration = utils.parse_duration(duration_str)
    except Exception as e:
        print("Error parsing duration:", e)
        sys.exit(1)

    unlock_time = datetime.datetime.now() + duration
    unlock_time_str = unlock_time.isoformat()

    # Hash password
    salt, pwd_hash = password_storage.hash_password(password)

    # Lock /etc/hosts
    if not lock_control.lock_hosts():
        print("Failed to lock /etc/hosts.")
        sys.exit(1)
    
    # Save state (store hash and salt as hex strings)
    state_data = {
        "password_hash": pwd_hash.hex(),
        "salt": salt.hex(),
        "lock_until": unlock_time_str,
        "is_locked": True
    }
    config.save_state(state_data)
    
    # Schedule auto-unlock
    if not scheduler.schedule_unlock(unlock_time):
        print("Warning: failed to schedule auto-unlock. You must unlock manually.")
    print(f"/etc/hosts is now locked until {unlock_time_str}.")

def unlock(manual=True):
    state = config.load_state()
    if not state or not state.get("is_locked"):
        print("No active lock found.")
        return

    if manual:
        password = getpass("Enter unlock password: ")
    else:
        # Auto-unlock mode does not require a password
        password = None

    # For manual unlock, verify password
    if manual:
        stored_hash = bytes.fromhex(state.get("password_hash"))
        salt = bytes.fromhex(state.get("salt"))
        if not password_storage.verify_password(password, salt, stored_hash):
            print("Incorrect password. The hosts file remains locked.")
            sys.exit(1)

    if not lock_control.unlock_hosts():
        print("Failed to unlock /etc/hosts.")
        sys.exit(1)
    config.clear_state()
    print("/etc/hosts has been unlocked.")

def status():
    state = config.load_state()
    if state and state.get("is_locked"):
        print("The hosts file is locked until {}.".format(state.get("lock_until")))
    else:
        print("The hosts file is not locked.")

def main():
    check_root()
    
    parser = argparse.ArgumentParser(
        description="Ubuntu Hosts File Locking Utility",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--lock", action="store_true", help="Lock /etc/hosts")
    group.add_argument("--unlock", action="store_true", help="Unlock /etc/hosts manually")
    group.add_argument("--status", action="store_true", help="Show lock status")
    group.add_argument("--auto-unlock", action="store_true", help=argparse.SUPPRESS)  # internal use for auto-unlock

    args = parser.parse_args()

    if args.lock:
        lock()
    elif args.unlock:
        unlock(manual=True)
    elif args.status:
        status()
    elif args.auto_unlock:
        unlock(manual=False)

if __name__ == "__main__":
    main()
