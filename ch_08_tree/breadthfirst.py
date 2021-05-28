# Created by Ellie Le at 5/25/2021

from linked_queue import LinkedQueue

def breadthfirst(self):
    """Generate a breadth-first iteration of the positions of the tree."""
    if not self.is_empty():
        fringe = LinkedQueue()                      # known positions not yet yielded
        fringe.enqueue(self.root())                 # starting with the root
        while not fringe.is_empty():
            p = fringe.dequeue()                    # remove from front of the queue
            yield p                                 # report this position
            for c in self.children(p):
                fringe.enqueue(c)                   # add children to back of the queue

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:                # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                                     # visit p between its subtrees
        if self.right(p) is not None:               # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other


    # Support for performing an inorder traversal of a binary tree.

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()                       # make inorder the default

