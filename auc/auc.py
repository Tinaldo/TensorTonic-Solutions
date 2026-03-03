import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    fpr = np.asarray(fpr, dtype=float)
    tpr = np.asarray(tpr, dtype=float)

    fpr_size = fpr.size
    tpr_size = tpr.size

    if fpr_size != tpr_size:
        raise ValueError("Arrays are not of the same length")

    if fpr_size < 2 or tpr_size < 2:
        raise ValueError("Arrays must be of length at least 2")

    auc = np.trapezoid(tpr, fpr)

    return auc