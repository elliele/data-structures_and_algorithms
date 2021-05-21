# Created by Ellie Le at 5/20/2021
"""
The new FavoritesListMTF class inherits most of its functionality
from the original FavoritesList as a base class.
By our original design, the access method of the original class relies on a nonpublic
utility named move up to enact the potential shifting of an element forward
in the list, after its access count had been incremented. Therefore, we implement
the move-to-front heuristic by simply overriding the move up method so that each
accessed element is moved directly to the front of the list (if not already there). This
action is easily implemented by means of the positional list ADT.
The more complex portion of our FavoritesListMTF class is the new definition
for the top method. We rely on the first of the approaches outlined above, inserting
copies of the items into a temporary list and then repeatedly finding, reporting, and
removing an element that has the largest access count of those remaining
"""

from FavoriteList import FavoriteList
from PositionalList import PositionalList

class FavoritesListMTF(FavoriteList):
    """List of elements ordered with move-to-front heuristic."""

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))                  # delete/reinsert

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # we begin by making copy of the original list
        temp = PositionalList()
        for item in self._data:                                            # positional lists support iteration
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with the highest count
            yield highPos.element()._value
            temp.delete(highPos)