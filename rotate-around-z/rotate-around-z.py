import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    points = np.asarray(points, dtype=float)
    cos = np.cos(theta)
    sin = np.sin(theta)
    R = np.array([
        [cos, -sin, 0],
        [sin, cos, 0 ],
        [0, 0, 1]
    ])

    return points @ R.T