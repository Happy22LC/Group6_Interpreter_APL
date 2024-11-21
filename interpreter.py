from ast_nodes import AssignNode, PrintNode, BinOpNode, VarNode

''' 

class Environment:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value
        print(f"Environment updated: {name} = {value}")  # Debugging

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        raise NameError(f"Variable '{name}' is not defined")


class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = Environment()

    def interpret(self):
        print("Interpreter: Starting interpretation")  # Debugging
        for node in self.ast:
            self._evaluate(node)

    def _evaluate(self, node):
        node_type = node['type']
        print(f"Evaluating node: {type(node).__name__}")  # Debugging
        if node_type == 'let':
            self._evaluate_let(node)
        elif node_type == 'print':
            self._evaluate_print(node)
        elif node_type == 'binop':
            return self._evaluate_binop(node)
        elif node_type == 'number':
            return node['value']
        elif node_type == 'id':
            return self.env.get_variable(node['value'])
        else:
            raise ValueError(f"Unknown node type: {node_type}")

    def _evaluate_let(self, node):
        var_name = node['name']
        value = self._evaluate(node['value'])
        self.env.set_variable(var_name, value)

    def _evaluate_print(self, node):
        value = self._evaluate(node['value'])
        print(value)

    def _evaluate_binop(self, node):
        left = self._evaluate(node['left'])
        right = self._evaluate(node['right'])
        op = node['op']

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
            I changed the original _evaluate method and its related methods because it assumed that each node in the AST was represented as a dictionary 
            (e.g., node['type'], node['value'], etc.). However, in your actual implementation, the nodes are instances of custom classes (e.g., AssignNode, BinOpNode, NumNode), 
            not dictionaries. This means you cannot use dictionary-style subscripting (node['type'] or node['value']), and instead, you need to access the attributes of these
             objects using dot notation (e.g., node.var_name or node.expr).
            
            Node Representation: The nodes in your AST (AssignNode, BinOpNode, etc.) are custom objects, 
            not dictionaries. Therefore, you must use dot notation to access their attributes. 
            
            Consistency: Your entire codebase (from Parser to AST) is object-oriented. Keeping the Interpreter in line with this design 
            makes the code more readable and maintainable. 
            
            Avoid Runtime Errors: Using node['type'] or node['value'] 
            on non-dictionary objects would result in a TypeError ('AssignNode' object is not subscriptable). 

'''
from ast_nodes import AssignNode, PrintNode, BinOpNode, NumNode, VarNode


# Environment class to manage variable storage
class Environment:
    def __init__(self):
        self.variables = {}  # Dictionary to store variable names and their values

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
        # Determine the type of the node and evaluate it accordingly
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
        # Evaluate a variable assignment
        var_name = node.var_name  # Get the variable name
        value = self._evaluate(node.expr)  # Evaluate the expression
        self.env.set_variable(var_name, value)  # Store the variable in the environment

    def _evaluate_print(self, node):
        # Evaluate and print an expression
        value = self._evaluate(node.expr)  # Evaluate the expression
        # print(value)  # Print the result
        print(f"Value : {value}")

    def _evaluate_binop(self, node):
        # Evaluate a binary operation
        left = self._evaluate(node.left)  # Evaluate the left-hand side
        right = self._evaluate(node.right)  # Evaluate the right-hand side
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
