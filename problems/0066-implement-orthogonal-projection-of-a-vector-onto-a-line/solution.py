
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    num = sum(x*y for x,y in zip(L,v))
    denom = sum(x*x for x in L)
    for i in range(len(L)):
        L[i] = num/denom * L[i]

    return L
    pass
