import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)
    # print(x-y)
    # print(abs(x-y))
    return np.sum(np.abs(x-y))