import math
import numpy as np

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    r = []
    for num in x:
        if num > 0:
            r.append(num)
        else:
            r.append(alpha * (math.exp(num) - 1))

    return r