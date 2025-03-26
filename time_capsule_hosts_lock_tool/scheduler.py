import subprocess
import datetime

def schedule_unlock(unlock_time: datetime.datetime):
    """
    Schedule an auto-unlock using the 'at' command.
    This will run: python3 -m hosts_lock_tool.cli --auto-unlock
    at the specified unlock time.
    """
    # Format unlock_time for the 'at' command: "HH:MM YYYY-MM-DD"
    at_time = unlock_time.strftime("%H:%M %Y-%m-%d")
    command = "python3 -m hosts_lock_tool.cli --auto-unlock"
    try:
        # Schedule the command by piping it to 'at'
        proc = subprocess.run(['at', at_time],
                              input=command.encode(),
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              check=True)
        return True
    except subprocess.CalledProcessError as e:
        print("Error scheduling unlock:", e.stderr.decode())
        return False
