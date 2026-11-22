import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    if type(x) == int:
        return 1 / (1 + np.exp(-x))
    r = []
    x = np.array(x)
    for num in x:
        r.append(1 / (1 + np.exp(-num)))
    return r
    # print()