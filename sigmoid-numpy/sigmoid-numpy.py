import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """

    sigma = 1/(1+np.exp(-np.asarray(x, dtype=float)))
    # Write code here
    return sigma