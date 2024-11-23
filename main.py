# main.py

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def main():
    print("Enter your code (use ';' to separate statements) & type (output) to get the result :")
    code = ""
    while True:
        try:
            line = input(">>> ")
        except EOFError:
            break
        if line.strip() == "output":
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
        print("\nLexical Analysis : ")
        print(f"Tokens: {tokens}")

        # Parsing
        parser = Parser(tokens)
        tree = parser.parse()
        print("\nParsing : ")
        print(f"AST-Tree : {tree}")

        # Interpretation
        interpreter = Interpreter(tree)
        print("\nInterpretation : ")
        interpreter.interpret()
    except Exception as e:
        print("Invalid input. Please check your provided code.")
        print(e)


if __name__ == "__main__":
    main()
