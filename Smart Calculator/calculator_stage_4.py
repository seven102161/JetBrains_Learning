def rewrite_content(string):
    string = string.replace('--', '+')
    string = string.replace('---', '-')
    string = string.replace('+', ' ')
    return string


def calculation(string):
    string = string.split()
    operator = 'add'
    result = 0

    for i in string:
        if i == '-':
            operator = 'minus'
        else:
            if operator == 'add':
                result += int(i)
            elif operator == 'minus':
                result -= int(i)
                operator = 'add'

    return result


def main():

    while True:
        expressions = input()
        if expressions == '/help':
            print('The program calculates the sum of numbers')
            continue

        if expressions == '/exit':
            print('Bye!')
            break

        if len(expressions) == 0:
            print(r'If you need help, you can write "/help"')
            continue

        new_expressions = rewrite_content(expressions)

        print(calculation(new_expressions))


if __name__ == '__main__':
    main()









