# Created by Ellie Le at 6/27/2021

"""In our implementation, we declare a class-level attribute, _AVAIL, as a sentinel.
(We use an instance of the built-in object class because we do not care about any behaviors of the sentinel,
just our ability to differentiate it from other objects.

We defined a nonpublic utility, _find_slot, that searches for an item with key k in
"bucket" j (that is, where j is the index returned by the hash function for k)."""


from HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()     # sentinal marks locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match fouond, success is False and index denotes first available slot."""

        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j          # mark this as first avail

                if self._table[j] is None:
                    return (False, firstAvail)      # search has failed
            elif k == self._table[j]._key:
                return (True, j)                    # found a match
            j = (j + 1) % len(self._table)          # keep looking (cyclically)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))     # no match found
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,v)            # insert new item
            self._n += 1                                # size has increased
        else:
            self._table[s] ._value = v                  # overwrite existing

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))           # no match found
        self._table[s] = ProbeHashMap._AVAIL                    # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):                   # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key
