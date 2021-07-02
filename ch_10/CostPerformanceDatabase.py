# Created by Ellie Le at 7/1/2021
"""
We can store the set of maxima pairs in a sorted map, M, so that the cost is the
key field and performance (speed) is the value field. We can then implement
operations add(c,p), which adds a new cost-performance pair (c,p), and best(c),
which returns the best pair with cost at most c.
"""
from SortedTableMap import SortedTableMap


class CostPerformanceDatabase:
    """Maintain a database of maximal (cost, performance) pairs."""

    def __init__(self):
        """Create an empty database."""
        self._M = SortedTableMap()                      # or a more efficient sorted map

    def best(self, c):
        """Return (cost, performance) pair with largset cost not exceeding c.

        Return None if there is no such pair"""
        return self._M.find_le(c)

    def add(self, c, p):
        """Add new entry with cost c and performance p."""
        #determine if (c,p) is dominated by an exisitng pair
        other = self._M.find_le(c)                      # other is at least as cheap as c
        if other is not None and other [1] >= p:        # if its performance is as good,
            return                                      # (c,p) is dominated, so ignore
        self._M[c] = p                                  # else, add (c,p) to database
        # add now remove any pairs that are dominated by (c,p)
        other = self._M.find_gt(c)                      # other more expensive than c
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
            
