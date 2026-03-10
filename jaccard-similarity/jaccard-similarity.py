def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a = set(set_a)
    set_b = set(set_b)

    if len(set_a) == 0 and len(set_b) == 0:
        return 0.0

    union = set_a | set_b
    intersection = set_a & set_b

    j = len(intersection)/len(union)

    return float(j)

    