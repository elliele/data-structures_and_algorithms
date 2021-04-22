# Created by Ellie Le at 4/21/2021
"""
Revisit the problem of summing the n elements of a sequence, S, of numbers.
With two or more elements, we can recursively compute the sum of the first half, and hte sum of the second half,
and add these sums together. Our implementation of such an algorithm, is initially invoked as
binary_sum(A, 0, len(A)).

"""

def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:                           # zero elements in slice
        return 0
    elif start == stop - 1:                     # one element in slice
        return S[start]
    else:
        mid = (start + stop) // 2               # two or more elements in slice
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

A = [*range(0, 8, 1)]
print(binary_sum(A,0,len(A)))

"""
Enumerate various configurations in order to solve a combinatorial puzzle.


To keep the description general enough to be used with other puzzles, the 
algorithm enumerates and tests all k-length sequences without repetitions of 
the elements of a given universe U. We build the sequences of k elements by the following steps:
1. Recursively generating the sequences of k−1 elements
2. Appending to each such sequence an element not already contained in it.

For summation puzzles, U = {0,1,2,3,4,5,6,7,8,9} and each position in the
sequence corresponds to a given letter. For example, the first position could stand
for b, the second for o, the third for y, and so on.

"""

