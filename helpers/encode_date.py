import numpy as np 

def encode_month_cyclic(months):
    """
    Encode month values (1–12) into cyclic sine and cosine components.
    Preserves the circular relationship between December and January.
    Returns two arrays: month_sin, month_cos.
    """
    arr = np.asarray(months, dtype=float)
    radians = 2 * np.pi * arr / 12
    return np.sin(radians), np.cos(radians)


def encode_day_cyclic(days):
    """
    Encode day-of-month values (1–31) into cyclic sine and cosine components.
    Preserves continuity between the end and start of a month.
    Returns two arrays: day_sin, day_cos.
    """
    arr = np.asarray(days, dtype=float)
    radians = 2 * np.pi * arr / 31
    return np.sin(radians), np.cos(radians)


def encode_weekday_cyclic(weekdays):
    """
    Encode weekday numbers (0–6, where Monday=0) into cyclic sine and cosine components.
    Ensures Sunday and Monday remain close in the representation space.
    Returns two arrays: weekday_sin, weekday_cos.
    """
    arr = np.asarray(weekdays, dtype=float)
    radians = 2 * np.pi * arr / 7
    return np.sin(radians), np.cos(radians)

