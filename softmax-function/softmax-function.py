import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # convert input into np array type
    x = np.asarray(x , dtype = float)

    if x.ndim == 1:
        m = np.max(x)
        exp_values = np.exp(x - m)
        return exp_values / exp_values.sum()
    elif x.ndim == 2:
        m = np.max(x , axis = 1 , keepdims = True)
        exp_values = np.exp(x - m)
        return exp_values / exp_values.sum(axis = 1 , keepdims = True)
    else:
        raise ValueError("Input must be 1D or 2D")