# Created by Ellie Le at 4/11/2021

""""
Sequence abstract base class defines behaviors common to Python's list,
str, and tuple classes, as sequences that support element access via
an integer index. Sequence class provides concrete implementations of methods, count,
index, and __contains__ that can be inherited by any class that provides concrete
implementations of both __len__ and __getitem__.
"""

from abc import ABCMeta, abstractmethod                 # need these definitions


class Sequence(metaclass=ABCMeta):
    """Our own version of collections. Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        "Return the element at index j of the sequence."

    def __contains__(self, val):
        """Return leftmost index at which val is found (or raise ValueError)"""
        for j in range(len(self)):                      # leftmost match
            if self[j] == val:
                return j
            raise ValueError('value not in sequence')   # never found a match

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:                          # found a match
                k += 1
            return k