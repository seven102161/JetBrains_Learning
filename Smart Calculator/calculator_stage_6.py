def command_check(expression):
    if expression == '/exit':
        print('Bye!')
        return 'exit'

    if expression == '/help':
        print('The program calculates the sum of numbers')
        return 'help'

    return None


def variables_store(expression):
    global vars_stored
    result = None
    key, val = expression.split('=')
    key = key.strip()
    for i in key:
        if not i.isalpha():
            print('Invalid identifier')
            result = 'wrong'
            break
    if result is None:
        val = val.strip()
        try:
            val = int(val)
            vars_stored[key] = val
        except ValueError:
            for j in val:
                if j.isdigit():
                    print('Invalid assignment')
                    result = 'wrong'
                    break
            if result is None:
                if val in vars_stored.keys():
                    vars_stored[key] = vars_stored[val]
                else:
                    print('Unknown variable')
                    result = 'wrong'

    return result


def expression_refactoring(expression):
    # rewrite expression
    expression = expression.replace('--', '+')
    expression = expression.replace('---', '-')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    expression = expression.split()

    result = None
    for i in range(len(expression)):
        if expression[i] in ['+', '-']:
            continue
        if expression[i].isdigit():
            continue
        else:
            if valid_variable(*expression[i]) == 'wrong':
                print('Invalid identifier')
                result = 'wrong'
                break
            if expression[i] not in vars_stored.keys():
                result = 'wrong'
                print('Unknown variable')
                break
            if expression[i] in vars_stored.keys():
                expression[i] = str(vars_stored[expression[i]])

    if result == 'wrong':
        return None
    else:
        return expression


def valid_variable(*args):
    result = None
    digit_count = 0
    alpha_count = 0
    for i in args:
        if i.isdigit():
            digit_count += 1
        else:
            alpha_count += 1
    if digit_count > 0 and alpha_count > 0:
        result = 'wrong'
    return result


def calculation(expression):
    result = 0
    operator = '+'
    pre_element = 'operator'

    for element in expression:
        if pre_element == 'digit':
            if element.isdigit():
                result = 'Invalid expression'
            else:
                operator = element
                pre_element = 'operator'

        elif pre_element == 'operator':
            if element.isdigit():
                if operator == '+':
                    result += int(element)
                else:
                    result -= int(element)
                pre_element = 'digit'
            else:
                operator = element
                pre_element = 'operator'

    return result


def main():

    while True:
        expression = input()

        # command check
        command = command_check(expression)
        if command == 'exit':
            break
        elif command == 'help':
            continue
        elif command is None:
            pass

        if len(expression) == 0:
            continue

        # Variable assignment
        if expression.count('=') == 1:
            variables_store(expression)
            continue
        if expression.count('=') > 1:
            print('Invalid assignment')
            continue

        # expression rewrite and calculate
        expression = expression_refactoring(expression)
        if expression is None:
            continue
        else:
            print(calculation(expression))


if __name__ == '__main__':
    vars_stored = dict()
    main()
