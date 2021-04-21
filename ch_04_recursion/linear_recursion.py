# Created by Ellie Le at 4/20/2021

"""
A recursive algorithm for computing the sum of a sequence of numbers.
"""

def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

S = [4,3,6,2,8,9,3,2,8,5,1,7,2,8,3,7]
n = len(S)
print(linear_sum(S, n))