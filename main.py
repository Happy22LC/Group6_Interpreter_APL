''' from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def main():
    # This is the main loop for the interpreter. It continuously takes input from the user.
    while True:
        code = input("Enter code (or type 'exit' to quit): ")
        if code.lower() == 'exit':
            break

        lexer = Lexer(code)
        try:
            # Tokenize the input code
            tokens = lexer.tokenize()
            print("Tokens:", tokens)  # display tokens
            # Parse the tokens to generate the Abstract Syntax Tree (AST)
            parser = Parser(tokens)
            statements = parser.parse()

            # Pass the parsed AST (statements) to the Interpreter
            interpreter = Interpreter(statements)
            interpreter.interpret()  # Interpret the parsed statements
        except SyntaxError as e:
            print("Error:", e)  # Catch and display syntax errors
        except Exception as e:
            print("Runtime Error:", e)  # Catch and display other runtime errors


if __name__ == "__main__":
    main() '''


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
                var_name = statements[0].var_name  # Get the variable name from the first assignment
                print_statement = f"print({var_name});"
                # print(f"Automatically prompting for: {print_statement}")
                code = input(f"Prompt to print: ")

                # Tokenize and parse the auto-generated print statement
                print_tokens = Lexer(print_statement).tokenize()
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


