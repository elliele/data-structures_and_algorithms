# Created by Ellie Le at 5/25/2021

"""
The parenthetic string
representation P(T) of tree T is recursively defined as follows. If T consists of a
single position p, then

P(T) = str(p.element()).

Otherwise, it is defined recursively as,

P(T) = str(p.element())+ ( +P(T1)+ , + · · · + , +P(Tk)+ )

where p is the root of T and T1,T2, . . . ,Tk are the subtrees rooted at the children
of p, which are given in order if T is an ordered tree. We are using “+” here to
denote string concatenation. As an example, the parenthetic representation of the
tree of Figure 8.2 would appear as follows (line breaks are cosmetic):

Electronics R’Us (R&D, Sales (Domestic, International (Canada,
S. America, Overseas (Africa, Europe, Asia, Australia))),
Purchasing, Manufacturing (TV, CD, Tuner))
"""

def parenthesize(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')                      # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else', '       # determine proper separator
            print(sep, end='')
            first_time = False                      # any future passes with not be the first
            parenthesize(T, c)                      # recur on child
        print(')', end ='')                         # include closing parenthesis
