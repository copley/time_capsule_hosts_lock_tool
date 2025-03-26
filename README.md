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

