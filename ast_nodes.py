class ASTNode:
    pass


# Represents a variable assignment
class AssignNode(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr


# Represents a binary operation
class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


# Represents a number literal
class NumNode(ASTNode):
    def __init__(self, value):
        self.value = value


# Represents a variable
class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name


# Represents a print statement
class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr
