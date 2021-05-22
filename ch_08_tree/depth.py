# Created by Ellie Le at 5/22/2021


def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
        return 0
    return 1 + self.depth(self.parent(p))
