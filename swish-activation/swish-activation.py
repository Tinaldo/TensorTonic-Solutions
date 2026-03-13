import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    x_clip = np.clip(x, -500, 500)
    return x / (1 + np.exp(-x_clip))