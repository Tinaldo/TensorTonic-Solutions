import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here

    x = np.asarray(x)
    if p < 0 or p >= 1:
        raise ValueError("p must be in [0,1)")

    if x.shape > (1000, 1000):
        raise ValueError("Input array up to shape (1000, 1000)")
    
    rng = np.random.default_rng() if rng is None else rng
    dropout_pattern = rng.random(x.shape) < (1 - p)
    dropout_pattern =  dropout_pattern.astype(float) / (1-p)
    output = x * dropout_pattern
    
    return (output, dropout_pattern)