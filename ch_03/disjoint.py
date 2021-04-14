# Created by Ellie Le at 4/13/2021

"""
Suppose we are given three sequences of numbers, A, B, and C. We will assume
that no individual sequence contains duplicate values, but that there may be some
numbers that are in two or three of the sequences. The three-way set disjointness
problem is to determine if the intersection of the three sequences is empty, namely,
that there is no element x such that x ∈ A, x ∈ B, and x ∈ C.
"""

def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False        # we found a common value
    return True                         # if we reach this, sets are disjoint


def disjoint2(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            if a == b:
                for c in C:             # only check C if we found match from A and B
                    if a == c:          # (and thus a == b == c)
                        return False    # we found a common value
    return True                         # if we reach this, sets are disjoint
