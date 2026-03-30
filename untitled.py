def evaluate_postfix(expr):
    stack = []

    for token in expr:

        # Numbers
        if token.isdigit():
            stack.append(int(token))

        # Boolean values
        elif token in ["True", "False"]:
            stack.append(token == "True")

        # Comparison operators
        elif token == "<":
            b = stack.pop()
            a = stack.pop()
            stack.append(a < b)

        elif token == ">":
            b = stack.pop()
            a = stack.pop()
            stack.append(a > b)

        elif token == "<=":
            b = stack.pop()
            a = stack.pop()
            stack.append(a <= b)

        elif token == ">=":
            b = stack.pop()
            a = stack.pop()
            stack.append(a >= b)

        elif token == "==":
            b = stack.pop()
            a = stack.pop()
            stack.append(a == b)

        elif token == "!=":
            b = stack.pop()
            a = stack.pop()
            stack.append(a != b)

        # Logical operators
        elif token == "and":
            b = stack.pop()
            a = stack.pop()
            stack.append(a and b)

        elif token == "or":
            b = stack.pop()
            a = stack.pop()
            stack.append(a or b)

        elif token == "not":
            a = stack.pop()
            stack.append(not a)

    return stack.pop()

expr = ["5", "3", ">", "2", "1", "<", "and"]
print(evaluate_postfix(expr))