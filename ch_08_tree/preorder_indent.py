# Created by Ellie Le at 5/25/2021

"""
Produce an indented table of contents using a top-down recursion that includes the current depth as an additional
parameter.
"""

def preorder_indent(T, p, d):
    """Print preorder representation of subtree of T rooted at p at depth d."""
    print(2*d*' ' + str(p.element()))                       # use depth for indentation
    for c in T.children(p):
        preorder_indent(T, c, d+ 1)                         # child depth is d + 1
