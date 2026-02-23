import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)

    if (len(x) != len(y)):
        raise ValueError("Array not of the same size")
    
    return np.sqrt(np.sum((x-y)**2))