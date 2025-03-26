import re
from datetime import timedelta

def parse_duration(duration_str: str) -> timedelta:
    """
    Parse a duration string (e.g., "2h", "120m", "1d") and return a timedelta.
    """
    pattern = r"^(\d+)([hmd])$"
    match = re.match(pattern, duration_str.strip().lower())
    if not match:
        raise ValueError("Invalid duration format. Use format like '2h', '120m', or '1d'.")
    value, unit = match.groups()
    value = int(value)
    if unit == "h":
        return timedelta(hours=value)
    elif unit == "m":
        return timedelta(minutes=value)
    elif unit == "d":
        return timedelta(days=value)
    else:
        raise ValueError("Invalid time unit. Use h (hours), m (minutes), or d (days).")
