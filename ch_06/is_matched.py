# Created by Ellie Le at 4/30/2021

"""An Algorithm for matching delimiters.
Example:
    • Correct: ( )(( )){([( )])}
    • Correct: ((( )(( )){([( )])}))
    • Incorrect: )(( )){([( )])}
    • Incorrect: ({[ ])}
    • Incorrect: (
"""

def is_matched(expr):
    from array_stacks import ArrayStack

    """Return True if all delimiters are properly match; False otherwise."""
    lefty ='({['                    # opening delimiters
    righty = ')}]'                  # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)               # push left limiter on stack
        elif c in righty:
            if S.is_empty():
                return False        # nothing to match
            if righty.index(c) != lefty.index(S.pop()):
                return False        # mismatched
    return S.is_empty()         # were all symbols matched?

print(is_matched('[(5+x)-(y+z)]'))