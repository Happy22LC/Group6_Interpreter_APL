from ast_nodes import *


class Parser:
    def __init__(self, tokens):
        # Initialize the parser with a list of tokens
        self.tokens = tokens
        self.pos = 0  # Keeps track of the current position in the token list

    def parse(self):
        # Parse multiple statements into an AST
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self._parse_statement())
        return statements

    def _parse_statement(self):
        # Parse a single statement based on the current token
        current_token = self._peek()
        if current_token[0] == 'LET':
            return self._parse_assignment()
        elif current_token[0] == 'PRINT':
            return self._parse_print()
        else:
            raise SyntaxError(f"Unexpected token: {current_token}")

    def _parse_assignment(self):
        # Parse variable assignment statements
        self._expect('LET')
        var_name = self._expect('ID')[1]
        self._expect('ASSIGN')
        expr = self._parse_expression()
        self._expect('SEMI')
        return AssignNode(var_name, expr)

    def _parse_print(self):
        # Parse print statements
        self._expect('PRINT')
        expr = self._parse_expression()
        self._expect('SEMI')
        return PrintNode(expr)

    def _parse_expression(self):
        # Parse expressions with addition and subtraction
        left = self._parse_term()
        while self._peek()[0] in ('PLUS', 'MINUS'):
            # op = self._next()[0]
            # The commented-out code (# op = self._next()[0]). extracts the wrong part of the
            # token (the type, 'PLUS'). Since the AST needs the actual operator ('+'), the corrected code ensures the
            # proper value is used.
            op_token = self._next()
            op = op_token[1]  # Use the actual operator character ('+' or '-')
            right = self._parse_term()
            left = BinOpNode(left, op, right)
        return left

    def _parse_term(self):
        # Parse terms with multiplication and division
        left = self._parse_factor()
        while self._peek()[0] in ('MUL', 'DIV'):
            # op = self._next()[0]
            op_token = self._next()
            op = op_token[1]  # Use the actual operator character ('*' or '/')
            right = self._parse_factor()
            left = BinOpNode(left, op, right)
        return left

    def _parse_factor(self):
        # Parse individual factors (numbers, variables, or expressions in parentheses)
        current_token = self._next()
        if current_token[0] == 'NUMBER':
            return NumNode(current_token[1])
        elif current_token[0] == 'ID':
            return VarNode(current_token[1])
        elif current_token[0] == 'LPAREN':
            expr = self._parse_expression()
            self._expect('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Unexpected token: {current_token}")

    def _peek(self):
        # Peek at the current token without advancing
        return self.tokens[self.pos]

    def _next(self):
        # Get the current token and advance the position
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def _expect(self, token_type):
        # Expect a specific type of token, raise an error if it doesn't match
        token = self._next()
        if token[0] != token_type:
            raise SyntaxError(f"Expected {token_type}, got {token}")
        return token
