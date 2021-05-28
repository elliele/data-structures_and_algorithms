# Created by Ellie Le at 5/24/2021

def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()):           # start recursion
            yield p


def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p                                                     # visit p before its subtrees
    for c in self.children(p):                                  # for each child in c
        for other in self._subtree_preorder(c):                 # do preorder of c's subtree
            yield other                                         # yielding each to our caller

def positions(self):
    """Generate an interation of the tree's positions."""
    return self.preorder()                                      # return entire preorder iteration
