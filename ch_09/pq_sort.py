# Created by Ellie Le at 6/3/2021

from PriorityQueueBase import PriorityQueueBase
def pq_sort(C):
    """Sort a colletion of elements stored in a positional list."""
    n = len(C)
    P = PriorityQueueBase()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)                 # use element as key and value
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)                           # store smallest remaining element in C
