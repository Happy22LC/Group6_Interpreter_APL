class ASTNode:
    pass


# Represents a variable assignment
class AssignNode(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

    # The __repr__ method in each class ensures that this format is followed when the node is printed or logged.
    def __repr__(self):
        return f"AssignNode(var={self.var_name}, expr={repr(self.expr)})"


# Represents a binary operation
class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOpNode(left={repr(self.left)}, op={self.op}, right={repr(self.right)})"


# Represents a number literal
class NumNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumNode(value={self.value})"


# Represents a variable
class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VarNode(name={self.name})"


# Represents a print statement
class PrintNode:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"PrintNode(expr={repr(self.expr)})"
