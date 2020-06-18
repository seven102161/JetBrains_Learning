def rewrite_content(string):
    string = string.replace('--', '+')
    string = string.replace('---', '-')
    string = string.replace('+', '')
    return string


def calculation(string):
    content_list = list(string)

    minus_sign_list = []
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

    n = rewrite_content(expressions)
    print(calculation(n))


