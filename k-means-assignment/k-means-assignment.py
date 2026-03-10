def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """

    dim = len(points[0])
    num_centroids = len(centroids)
    num_points = len(points)
    assignments = [0] * num_points

    for i, point in enumerate(points):
        temp = [0.0] * num_centroids
        for j, centroid in enumerate(centroids):
            for d in range(dim):
                temp[j] += (point[d] - centroid[d])**2
        assignments[i] = temp.index(min(temp))

    return assignments