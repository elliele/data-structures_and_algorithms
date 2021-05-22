# Created by Ellie Le at 5/22/2021

def _height1(self):
    """Return the height of the tree."""
    return max(self.depth(p) for p in self.positions() if self.is_lead(p))

def height2(self, p):
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.children(p))

def height(self, p=None):
    """Return the height of the subtree rooted at Position p.

    if p is None, return the height of the entire tree.
    """
    if p is None:
        p = self.root()
    return self.height2(p)