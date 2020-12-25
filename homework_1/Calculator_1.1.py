
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
            with open("loggs.txt", 'a') as f:
                f.write(f'\nExpression: {expression}\nERROR: Invalide expression\nReport: INFO-{INFO}, ERROR-{ERROR}\n')
            return

    INFO += 1
    res = stack.pop()
    print(f'Result: {res}')
    with open("loggs.txt", 'a') as f:
        f.write(f'\nExpresion: {expression}\nResult: {res}\nReport: INFO-{INFO}, ERROR-{ERROR}\n')


if __name__ == "__main__":
    while True:
        msg = "CALCULATOR"
        print(f'{msg:=^50}')
        print("1) Start")
        print("2) Quit")
        option = input("Select the option - ")
        if option == '1':
            exeption = input("Exeption: ")
            PrefixEvaluate(exeption)
        elif option == '2':
            break
        else:
            print("OPTION ERROR, try again")
