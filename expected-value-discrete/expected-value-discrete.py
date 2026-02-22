import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)
    
    if not np.allclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Sum of probabilities is different to 1")
    else:
        return np.sum(x * p)
    
