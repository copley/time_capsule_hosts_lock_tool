import subprocess

HOSTS_FILE = "/etc/hosts"

def lock_hosts():
    try:
        # Set the immutable flag on /etc/hosts
        subprocess.run(["chattr", "+i", HOSTS_FILE], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print("Error locking hosts file:", e.stderr.decode())
        return False

def unlock_hosts():
    try:
        # Remove the immutable flag from /etc/hosts
        subprocess.run(["chattr", "-i", HOSTS_FILE], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print("Error unlocking hosts file:", e.stderr.decode())
        return False

def is_locked():
    try:
        result = subprocess.run(["lsattr", HOSTS_FILE], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        # The immutable flag is represented by an 'i' in the attribute string
        return "i" in output.split()[0]
    except subprocess.CalledProcessError as e:
        print("Error checking hosts file attributes:", e.stderr.decode())
        return False
