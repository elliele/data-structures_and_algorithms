# Created by Ellie Le at 5/22/2021

from Tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #--------------- additional abstract methods ------------------
    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child."""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child."""
        raise NotImplementedError('must be implemented by subclass')
    # --------------- concrete methods implemented in this class ------------------
    def siblings(self, p):
        """Return a Position representing p's siblings (or None if no siblings)."""
        parent = self.parent(p)
        if parent is None:                          # p must be the root
            return None                             # root has no siblings
        else:
            if p == self.left(parent):
                return self.right(parent)           # possibly None
            if p == self.right(parent):             # possibly None
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    
