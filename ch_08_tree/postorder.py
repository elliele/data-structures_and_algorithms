# Created by Ellie Le at 5/24/2021


def postoder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_postorder(self.root()):              # start recursion
            yield p

def _subtree_postorder(self, p):
    """Generate a postorder iteration of positions in subtree rooted at p."""
    for c in self.children(p):                                      # for each child c
        for other in self._subtree_postorder(c):                    # do postorder of c's subtree
            yield other                                             # yield each to our caller
    yield p                                                         # visit p after its subtrees