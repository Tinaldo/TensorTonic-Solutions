import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v)

    if v.ndim == 1:
        norm_v = np.linalg.norm(v)
        if norm_v <= 1e-10:
            return np.zero_like(v, dtype=float)
        return v / norm_v
    else:
        norms = np.linalg.norm(v, axis=1, keepdims=True)
        norms = np.where(norms <= 1e-10, 1.0, norms)
        return v / norms

        
    