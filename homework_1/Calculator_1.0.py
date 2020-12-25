INFO = 0
ERROR = 0


def is_int_operand(c):

    return c.isdigit()


def is_float_operand(c):

    return c.replace('.', '', 1).isdigit()


def PrefixEvaluate(expression):

    stack = []
    operators = ['+', '-', '*', '/', "add", "sub", "mul", "div"]
    global INFO
    global ERROR

    for unknown in expression.split()[::-1]:

        if is_int_operand(unknown):
            stack.append(int(unknown))

        elif is_float_operand(unknown):
            stack.append(float(unknown))

        elif unknown in operators:

            operand1 = stack.pop()
            operand2 = stack.pop()

            if unknown == '+' or unknown == "add":
                stack.append(operand1 + operand2)

            elif unknown == '-' or unknown == "sub":
                stack.append(operand1 - operand2)

            elif unknown == '*' or unknown == "mul":
                stack.append(operand1 * operand2)

            elif unknown == '/' or unknown == "div":
                stack.append(operand1 / operand2)
        else:
            ERROR += 1
            print(f'ERROR: Invalid expression')
            print(f'Report: INFO-{INFO}, ERROR-{ERROR}')
            return

    INFO += 1
    print(f'Result: {stack.pop()}')
    print(f'Report: INFO-{INFO}, ERROR-{ERROR}')


# Driver code
if __name__ == "__main__":
    Expression = input("Expression: ")
    PrefixEvaluate(Expression)