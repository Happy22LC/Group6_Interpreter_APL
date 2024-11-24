from ast_nodes import AssignNode, PrintNode, BinOpNode, NumNode, VarNode


# Environment class to manage variable storage
class Environment:
    def __init__(self):
        self.variables = {}  # store variable names and their values

    def set_variable(self, name, value):
        # Store a variable in the environment
        self.variables[name] = value
        # print(f"Result : {name} = {value}")  # Debugging

    def get_variable(self, name):
        # Retrieve a variable's value from the environment
        if name in self.variables:
            return self.variables[name]
        # Raise an error if the variable is not defined
        raise NameError(f"Variable '{name}' is not defined")


# Interpreter class to evaluate the AST
class Interpreter:
    def __init__(self, ast):
        self.ast = ast  # The Abstract Syntax Tree (list of nodes)
        self.env = Environment()  # The environment to manage variables

    def interpret(self):
        # Start interpreting the AST
        # print("Interpreter: Starting interpretation")  # Debugging
        for node in self.ast:
            self._evaluate(node)  # Evaluate each node in the AST

    def _evaluate(self, node):
        # evaluate the type of the node
        if isinstance(node, AssignNode):  # Handle variable assignments
            self._evaluate_let(node)
        elif isinstance(node, PrintNode):  # Handle print statements
            self._evaluate_print(node)
        elif isinstance(node, BinOpNode):  # Handle binary operations
            return self._evaluate_binop(node)
        elif isinstance(node, NumNode):  # Handle numeric literals
            return node.value
        elif isinstance(node, VarNode):  # Handle variables
            return self.env.get_variable(node.name)
        else:
            # Raise an error for unknown node types
            raise ValueError(f"Unknown node type: {type(node).__name__}")

    def _evaluate_let(self, node):
        # evaluate variable assignment
        var_name = node.var_name  # Get the variable name
        value = self._evaluate(node.expr)  # Evaluate the expression
        self.env.set_variable(var_name, value)  # Store the variable in the environment

    def _evaluate_print(self, node):
        # Evaluate and print the expression
        value = self._evaluate(node.expr)  # Evaluate the expression
        # print(value)  # Debugging, Print the result
        print(f"Value : {value}")

    def _evaluate_binop(self, node):
        # Evaluate a binary operation
        left = self._evaluate(node.left)  # Evaluate left-hand side
        right = self._evaluate(node.right)  # Evaluate right-hand side
        op = node.op  # Get the operator

        # Perform the operation based on the operator
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return left / right
        else:
            raise ValueError(f"Unsupported operator: {op}")
