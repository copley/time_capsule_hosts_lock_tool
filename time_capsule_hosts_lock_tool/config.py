import os
import json

STATE_DIR = "/etc/hosts_lock_tool"
STATE_FILE_PATH = os.path.join(STATE_DIR, "config.json")

def ensure_state_dir():
    if not os.path.exists(STATE_DIR):
        try:
            os.makedirs(STATE_DIR, mode=0o700)
        except Exception as e:
            print("Error creating state directory:", e)
            raise

def load_state():
    ensure_state_dir()
    if not os.path.exists(STATE_FILE_PATH):
        return None
    try:
        with open(STATE_FILE_PATH, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print("Error loading state file:", e)
        return None

def save_state(state_data):
    ensure_state_dir()
    try:
        with open(STATE_FILE_PATH, "w") as f:
            json.dump(state_data, f)
        # Set file permissions to 600 (rw-------)
        os.chmod(STATE_FILE_PATH, 0o600)
    except Exception as e:
        print("Error saving state file:", e)

def clear_state():
    if os.path.exists(STATE_FILE_PATH):
        try:
            os.remove(STATE_FILE_PATH)
        except Exception as e:
            print("Error clearing state file:", e)
