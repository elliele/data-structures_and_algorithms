# Created by Ellie Le at 4/21/2021

def binary_search_iterative(data, target):
    """Return True if target is fund in the given Python list."""
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:                         # found a match
            return True
        elif target < data[mid]:
            high = mid - 1                              # only consider values left of mid
        else:
            low = mid + 1                               # only consider values right of mid
        return False                                    # loop ended without success

"""Nonrecursive implementation of the recursive reverse method."""

def reverse_iterative(S):
    """Reverse elements in sequence S."""
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop -1], S[start]     # swap first and last
        start, stop = start + 1, stop - 1                # narrow the range