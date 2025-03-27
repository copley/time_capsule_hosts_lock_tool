Time Capsule Hosts Lock Tool

Time Capsule Hosts Lock Tool is a command-line Python utility for Ubuntu Linux that locks your system’s /etc/hosts file by setting its immutable flag. The tool prevents any modifications until the specified duration expires or you manually unlock it using a secure password. An auto-unlock is also scheduled via the at command.

How to Run the App
1. Locking the Hosts File
From your project's root directory (the directory that contains the time_capsule_hosts_lock_tool folder), run the following command as root:

sudo python3 -m time_capsule_hosts_lock_tool.cli --lock
What Happens When You Run This Command:
Prompt for Password:
You’ll be asked to enter and confirm a password. This password will be required if you need to manually unlock the hosts file later.

Prompt for Lock Duration:
Next, you’ll enter the duration for which you want to lock /etc/hosts (for example, 2h for two hours).

Locking Process:
The app sets the immutable flag on /etc/hosts using chattr +i and schedules an auto-unlock with the at command.

2. Note on Auto-Unlock
Important:
The auto-unlock scheduler in time_capsule_hosts_lock_tool/scheduler.py originally referenced an old package name. To ensure auto-unlock works correctly, open time_capsule_hosts_lock_tool/scheduler.py and update the line:

command = "python3 -m hosts_lock_tool.cli --auto-unlock"
to:

command = "python3 -m time_capsule_hosts_lock_tool.cli --auto-unlock"
3. Unlocking the Hosts File
To manually unlock /etc/hosts, run:

sudo python3 -m time_capsule_hosts_lock_tool.cli --unlock
When prompted, enter the password you set during the lock process.

Summary
Lock the Hosts File:

sudo python3 -m time_capsule_hosts_lock_tool.cli --lock

(Optional) Update Auto-Unlock Command:
Edit time_capsule_hosts_lock_tool/scheduler.py to use:

command = "python3 -m time_capsule_hosts_lock_tool.cli --auto-unlock"
Unlock the Hosts File:

sudo python3 -m time_capsule_hosts_lock_tool.cli --unlock
This README outlines the steps to run and manage the locking mechanism on /etc/hosts from your project's root directory. If you encounter any issues, please check that your import paths and scheduler command are correctly configured as described above.
