import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    T = np.asarray(T, dtype=float)
    points = np.asarray(points, dtype=float)

    if points.ndim == 1:
        points = np.append(points, 1)
        points = T @ points
        points = np.delete(points, -1)
    else:
        arr = np.ones((points.shape[0], 1))
        points = np.hstack((points, arr))
        points = points @ T.T
        points = points[:, :-1]

    return points

    # Can be improved by doing shape validation for inputs 