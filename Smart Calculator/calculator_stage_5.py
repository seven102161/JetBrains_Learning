def rewrite_content(expression):
    expression = expression.replace('--', '+')
    expression = expression.replace('---', '-')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    return expression


def calculation(expression):
    expression = expression.split()
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

        if expression.startswith('/'):
            if expression == '/exit':
                print('Bye!')
                break

            elif expression == '/help':
                print('The program calculates the sum of numbers')
                continue

            else:
                print('Unknown command')
                continue

        if len(expression) == 0:
            print(r'If you need help, you can write "/help"')
            continue

        if expression.endswith('+') or expression.endswith('-'):
            print('Invalid expression')
            continue

        alpha = 0
        for i in expression:
            if i.isalpha():
                alpha += 1
        if alpha > 0:
            print('Invalid expression')
            continue

        print(calculation(rewrite_content(expression)))


if __name__ == '__main__':
    main()
