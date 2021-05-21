# Created by Ellie Le at 5/20/2021
"""
We wish to implement a favorites list by making use of a PositionalList for storage.
If elements of the positional list were simply elements of the favorites list, we
would be challenged to maintain access counts and to keep the proper count with
the associated element as the contents of the list are reordered. We use a general
object-oriented design pattern, the composition pattern, in which we define a single
object that is composed of two or more other objects. Specifically, we define a
nonpublic nested class, Item, that stores the element and its access count as a
single instance. We then maintain our favorites list as a PositionalList of item
instances, so that the access count for a user’s element is embedded alongside it in
our representation. (An Item is never exposed to a user of a FavoritesList.)
"""

from PositionalList import PositionalList

class FavoriteList:
    """List of elements ordered from most frequently accessed to least."""

    #--------------------------- nested _Item class ----------------------------
    class _Item:
        __slots__ = '_value', '_count'                      # streamline memory storage
        def __init__(self, e):
            self._value = e                                 # the user's element
            self._count = 0                                 # access count initially zero

    # --------------------------- nonpublic utilities ----------------------------
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p!= self._data.first():                           # consider moving ...
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:                 # must shift forward
                while (walk != self._data.first() and
                        cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))   # delete/reinsert

    # --------------------------- public methods ----------------------------
    def __init__(self):
        """Create an empty list of favorites."""
        self._data = PositionalList()                       # will be list of _Item instances

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty."""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)                          # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e))          # if new, place at end
        p.element()._count += 1                             # always increment count
        self._move_up(p)                                    # consider moving forward

    def remove(self, e):
        """Remove element e from list of favorites."""
        p = self._find_position(e)                          # try to locate existing element
        if p is not None:
            self._data.delete(p)                            # delete, if found

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()                           # element of list is _Item
            yield item._value                               # report user's element
            walk = self._data.after(walk)