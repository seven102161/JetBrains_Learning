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


def expression_refactoring():
    pass


def calculation():
    pass


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

        # Variable assignment check
        if expression.count('=') == 1:
            variables_store(expression)
            continue
        if expression.count('=') > 1:
            print('Invalid assignment')
            continue


if __name__ == '__main__':
    vars_stored = dict()
    main()
    print(vars_stored)

