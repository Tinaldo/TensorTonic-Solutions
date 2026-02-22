import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    np_x = np.asarray(x, dtype=float)
    verf = np.vectorize(math.erf)
    np_phi = (1.0 + verf(x/np.sqrt(2.0)))/2.0
    
    return np_x*np_phi
