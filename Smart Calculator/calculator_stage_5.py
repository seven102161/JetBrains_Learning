def expression_check(expression):
    valid_words_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ' ']
    for word in expression:
        if word not in valid_words_list:
            return False

    if expression.find('+') == -1 or expression.find('-') == -1:
        return False

    if expression.endswith('+') or expression.endswith('-'):
        return False


def command_check(expression):
    if expression == '/exit':
        return True
    elif expression != '/exit':
        return False


def rewrite_content(expression):
    expression = expression.replace('--', '+')
    expression = expression.replace('---', '-')
    return expression


def calculation(expression):
    content_list = list(expression)

    minus_sign_list = []
    # add_sign_list = []
    count = 0
    for i in content_list:
        if i == '-':
            minus_sign_list.append(count)
        else:
            content_list[i] = int(i)
        count += 1

    for i in minus_sign_list:
        content_list[i + 1] *= -1

    final_list = [i for i in content_list if i != '-']

    return sum(final_list)


def main():
    while True:
        expression = input()

        if expression.startswith(r'/'):
            if expression_check(expression):
                print('Bye!')
                break
            else:
                print('Unknown command')
                continue

        if expression_check(expression) is False:
            print('Invalid expression')
            continue

        print(calculation(rewrite_content(expression)))


if __name__ == '__main__':
    main()
