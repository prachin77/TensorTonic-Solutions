import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    s = len(v) #shape
    zeroes = np.zeros((s,s))
    for i in range(len(zeroes)):
        for j in range(len(zeroes[i])):
            if i == j:
                zeroes[i][j] = v[i]

    return zeroes