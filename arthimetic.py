# Arithmetic operators only: +, -, *, /

def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack.pop()


def evaluate_prefix(expression):
    stack = []
    tokens = expression.split()[::-1]

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack.pop()


# Example Usage
print(evaluate_postfix("2 3 * 5 4 * + 9 -"))   # 17
print(evaluate_prefix("- + * 2 3 * 5 4 9"))    # 17s