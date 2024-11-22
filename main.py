"""

from ast_nodes import AssignNode
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def main():

    # Initialize an interpreter with an empty AST
    interpreter = Interpreter([])  # Persistent environment across inputs

    while True:
        try:
            code = input("Enter code (or type 'exit' to quit): ")
            if code.lower() == "exit":  # Exit condition
                break

            # Tokenize the input
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            print("Tokens:", tokens)  # Debugging output

            # Parse the tokens into an AST
            parser = Parser(tokens)
            statements = parser.parse()

            # Update the interpreter with the new statements
            interpreter.ast = statements
            interpreter.interpret()  # Execute the statements

            # Automatically prompt for a print statement if it's an assignment
            if any(isinstance(stmt, AssignNode) for stmt in statements):
                code2 = input(f"Enter variable e.g.'print(a);' to display the output: ")
                lexer2 = Lexer(code2)

                # Tokenize and parse the auto-generated print statement
                print_tokens = lexer2.tokenize()
                print("Tokens:", print_tokens)  # Debugging output

                print_parser = Parser(print_tokens)
                print_statements = print_parser.parse()
                interpreter.ast = print_statements
                interpreter.interpret()  # Execute the print statement

        except SyntaxError as e:
            print("Syntax Error:", e)
        except Exception as e:
            print("Runtime Error:", e)


if __name__ == "__main__":
    main()
"""

# main.py

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def main():
    print("Enter your code (use ';' to separate statements, and type 'exit' to quit):")
    code = ""
    while True:
        try:
            line = input(">>> ")
        except EOFError:
            break  # Handle end-of-file (Ctrl+D)
        if line.strip() == "exit":
            break
        code += line + " "  # Accumulate the input code

    # Check if the code ends with a semicolon
    if not code.strip().endswith(';'):
        print("Syntax Error: Code must end with a semicolon (';').")
        return

    try:
        # Lexical Analysis
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        print("\n--- Lexical Analysis ---")
        print(f"Tokens: {tokens}")

        # Parsing
        parser = Parser(tokens)
        tree = parser.parse()
        print("\n--- Parsing ---")
        print(f"AST Tree: {tree}")

        # Interpretation
        interpreter = Interpreter(tree)
        print("\n--- Interpretation ---")
        interpreter.interpret()
    except Exception as e:
        print("Invalid input. Please check the code you typed.")
        print(e)


if __name__ == "__main__":
    main()
