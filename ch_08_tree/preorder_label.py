# Created by Ellie Le at 5/25/2021
"""
We might display the tree as follow:

Electronics R’Us
    1 R&D
    2 Sales
        2.1 Domestic
        2.2 International
            2.2.1 Canada
            2.2.2 S. America
"""

def preorder_label(T, p, d, path):
    """Print labeled representation of subtree of T rooted at p at depth d."""
    label =  '.'.join(str(j+1) for j in path)               # displayed labels are one-indexed
    print(2*d*' ' + label, p.element())
    path.append(0)                                          # path entries are zero-indexed
    for c in T.children(p):
        preorder_label(T, c, d+1, path)                     # child depth is d + 1
        path[-1] += 1
    path.pop()
