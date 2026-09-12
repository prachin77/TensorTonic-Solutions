import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A_conv = np.asarray(A)
    n_arr = A_conv.T
    return n_arr