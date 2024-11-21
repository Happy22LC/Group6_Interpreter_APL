class Lexer:
    def __init__(self, code):
        # Initialize the lexer with the input code and position tracker
        self.code = code
        self.pos = 0
        self.tokens = []   # List to store generated tokens

    def tokenize(self):
        # Tokenize the input code character by character
        while self.pos < len(self.code):
            current_char = self.code[self.pos]

            if current_char in ' \t\n\r':  # Skip whitespace
                self.pos += 1
                continue

            # Match operators and symbols
            elif current_char == '+':
                self.tokens.append(('PLUS', current_char))
            elif current_char == '-':
                self.tokens.append(('MINUS', current_char))
            elif current_char == '*':
                self.tokens.append(('MUL', current_char))
            elif current_char == '/':
                self.tokens.append(('DIV', current_char))
            elif current_char == '=':
                self.tokens.append(('ASSIGN', current_char))
            elif current_char == ';':
                self.tokens.append(('SEMI', current_char))
            elif current_char == '(':
                self.tokens.append(('LPAREN', current_char))
            elif current_char == ')':
                self.tokens.append(('RPAREN', current_char))

            # Match numbers
            elif current_char.isdigit():
                num = self._collect_number()
                self.tokens.append(('NUMBER', num))

            # Match identifiers (keywords or variable names)
            elif current_char.isalpha():
                ident = self._collect_identifier()
                if ident == 'let':
                    self.tokens.append(('LET', ident))
                elif ident == 'print':
                    self.tokens.append(('PRINT', ident))
                else:
                    self.tokens.append(('ID', ident))

            else:
                # Raise an error for unsupported characters
                raise SyntaxError(f'Unexpected character: {repr(current_char)} at position {self.pos}')

            self.pos += 1
        return self.tokens

    def _collect_number(self):
        # Helper function to extract a full number
        num_str = ''
        while self.pos < len(self.code) and self.code[self.pos].isdigit():
            num_str += self.code[self.pos]
            self.pos += 1
        self.pos -= 1  # Step back after collecting the full number
        return int(num_str)

    def _collect_identifier(self):
        # Helper function to extract a full identifier
        ident_str = ''
        while self.pos < len(self.code) and (self.code[self.pos].isalpha() or self.code[self.pos].isdigit()):
            ident_str += self.code[self.pos]
            self.pos += 1
        self.pos -= 1  # Step back after collecting the full identifier
        return ident_str
