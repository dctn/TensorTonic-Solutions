from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = sum(x) / len(x)
    mode = Counter(x).most_common(1)[0][0]
    
    sort = sorted(x)
    if len(sort)%2 == 0:
        median = float(sort[len(sort)//2 - 1] + sort[(len(sort)//2)]) / 2
        # print(sort[len(sort)//2])
    else:
        median = float(sort[round(len(sort)//2)])
    
    return { "mean": mean, "median": median, "mode": float(mode) }