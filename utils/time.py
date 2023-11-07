from datetime import datetime, timedelta

def _exceeded(t1: datetime, t2: datetime, threshold: timedelta) -> bool:
    """Check if the time difference between two datetime objects exceeds a threshold.

    Args:
        t1 (datetime): The first datetime object.
        t2 (datetime): The second datetime object.
        threshold (timedelta): The time threshold for comparison.

    Returns:
        bool: True if the time difference (t2 - t1) exceeds the threshold; otherwise, False.
    """
    if (t2 - t1) > threshold:
        return True
    return False
