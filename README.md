# Time Capsule Hosts Lock Tool

**Time Capsule Hosts Lock Tool** is a Python 3 terminal utility designed for Ubuntu Linux. It securely locks the system's `/etc/hosts` file, preventing modifications—even by root users—for a specified duration, effectively creating a time capsule for your hosts configuration.

This tool leverages the Linux immutable file attribute (`chattr +i`) and schedules automatic unlocking with the built-in `at` command. A secure password mechanism allows manual override if necessary.

---

## 🚀 Key Features

- **Immutable Locking**: Locks `/etc/hosts` against changes, deletion, or editing, even by users with root privileges.
- **Time Capsule Lock**: Specify a precise lock duration; the hosts file will auto-unlock at the expiration time.
- **Secure Password Protection**: Password-based override for immediate manual unlocking.
- **Auto-Unlock Scheduling**: Uses Linux's `at` scheduler to automatically unlock when the time capsule expires.

---

## ⚙️ Installation

Ensure you have Python 3 installed and the necessary system utilities (`chattr`, `at`). On Ubuntu, these utilities typically come pre-installed; otherwise, install with:

```bash
sudo apt install e2fsprogs at

# How to Run the Application

The tool provides an easy command-line interface. Follow these instructions:

## Locking `/etc/hosts`

To lock the hosts file, run the following command and follow the interactive prompts:

sudo hosts-lock --lock

markdown
Copy

You'll be asked to:
- Set and confirm a secure password (required for manual unlocking).
- Specify the lock duration (e.g., `2h` for 2 hours, `30m` for 30 minutes, `1d` for one day).

**Example:**

Enter lock password: Confirm lock password: Enter lock duration (e.g., 2h, 120m, 1d): 2h

perl
Copy

The hosts file will then become immutable for the specified duration.

## Manual Unlocking (Password Override)

If you need immediate access to edit `/etc/hosts` before the scheduled unlock time, use:

sudo hosts-lock --unlock

vbnet
Copy

You'll be prompted for the password set earlier.

## Checking Lock Status

To check if the `/etc/hosts` file is currently locked, run:

sudo hosts-lock --status

pgsql
Copy

The tool will inform you of the current lock state and unlock time if applicable.

---

🗒️ **License**

This project is licensed under the MIT License - see the LICENSE file for details.

⚠️ **Caution**

This utility is designed for convenience and deterrence, not as absolute security. Users with physical access or extensive system knowledge could potentially bypass the lock.
