# Created by Ellie Le at 5/28/2021

from LinkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expresison tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree.

        In a single parameter form, token should be a leaf value (e.g., '42'),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing Expression Tree instances
        that become the operands for the binary operator.
        """

        super().__init__()                  # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)               # use inherited, nonpublic method
        if left is not None:                # presumably three-parameter form
            if token not in '+-*x/':
                raise ValueError('token must be a valid operator')
            self._attach(self.root(), left, right)          # use inherited, nonpublic method

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []                         # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))                 # leaf value as a string
        else:
            result.append('(')                              # opening parenthesis
            self._parenthesize_recur(self.left(p), result)  # left subtree
            result.append(p.element())                      # operator
            self._parenthesize_recur(self.right(p), result) # right subtree
            result.append(')')                              # closing parenthesis

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted a p."""
        if self.is_leaf(p):
            return float(p.element())                       # we assume element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+': return left_val + right_val
            if op == '-': return left_val - right_val
            if op == '/': return left_val / right_val
            else: return left_val * right_val

