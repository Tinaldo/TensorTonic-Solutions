import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    fpr = np.asarray(fpr, dtype=float)
    tpr = np.asarray(tpr, dtype=float)

    if fpr.shape != tpr.shape:
        raise ValueError("Arrays are not of the same length")
    if fpr.size < 2:
        raise ValueError("Arrays must be of length at least 2")

    order = np.argsort(fpr)
    fpr = fpr[order]
    tpr = tpr[order]

    auc = np.trapezoid(tpr, fpr)

    return auc