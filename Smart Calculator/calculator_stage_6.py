def command_check(expression):
    if expression == '/exit':
        print('Bye!')
        return 'exit'

    if expression == '/help':
        print('The program calculates the sum of numbers')
        return 'help'

    return None


def variables_store():
    pass


def expression_refactoring():
    pass


def calculation():
    pass


def main():
    while True:
        expression = input()
        if command_check(expression) == 'exit':
            break
        elif command_check(expression) == 'help':
            continue
        elif command_check(expression) is None:
            pass


if __name__ == '__main__':
    main()

