import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """

    exp = np.exp(np.asarray(x, dtype=float))
    negexp = np.exp(-np.asarray(x, dtype=float))
    # Write code here
    return (exp - negexp)/(exp + negexp)