import numpy as np

def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    # Write code here
    if not (0.0 < beta1 < 1.0) or not (0.0 < beta2 < 1.0):
        raise ValueError("must be 0 < beta1, beta2 < 1")

    if lr <= 0 or eps <= 0:
        raise ValueError("must be lr > 0, eps > 0")
    
    w = np.asarray(w, dtype=float)
    m = np.asarray(m, dtype=float)
    v = np.asarray(v, dtype=float)
    grad = np.asarray(grad, dtype=float)

    new_m = beta1*m + (1 - beta1)*grad
    new_v = beta2*v + (1 - beta2)*grad**2
    new_w = w - lr*(beta1*new_m +(1-beta1)*grad)/(np.sqrt(new_v) + eps)

    return (new_w, new_m, new_v)