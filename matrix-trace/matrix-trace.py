import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == j:  
                sum += A[i][j]

    return float(sum)
    pass