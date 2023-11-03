

def dummy_func():
    print("Adding a new dummy function in the numpy open source code")

import numpy as np

def dot_product(a, b):
    """
    Calculate the dot product of two vectors.

    Parameters:
    a (ndarray): First vector.
    b (ndarray): Second vector.

    Returns:
    float: Dot product of the two vectors.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length.")
    return np.sum(a * b)
