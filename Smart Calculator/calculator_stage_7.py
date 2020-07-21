from collections import deque


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
    expression = expression.replace('---', '-')
    expression = expression.replace('--', '+')
    expression = expression.replace('+++', '+')
    expression = expression.replace('++', '+')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    expression = expression.replace('*', ' * ')
    expression = expression.replace('/', ' / ')
    expression = expression.replace('(', ' ( ')
    expression = expression.replace(')', ' ) ')
    expression = expression.split()

    return expression


def infix_to_postfix(expression):
    result = ''
    operators = ['+', '-', '*', '/', '(', ')']
    expression_queue = deque()
    operator_queue = deque()

    for i in expression:
        if i not in operators:
            expression_queue.append(i)
        elif len(operator_queue) == 0 or operator_queue[-1] == '(':
            operator_queue.append(i)
        else:
            if i in ['*', '/'] and operator_queue[-1] in ['+', '-']:
                operator_queue.append(i)
            elif i in ['*', '/'] and operator_queue[-1] in ['*', '/']:
                while True:
                    if len(operator_queue) == 0:
                        break
                    if operator_queue[-1] in ['+', '-']:
                        break
                    if operator_queue[-1] == '(':
                        break
                    expression_queue.append(operator_queue.pop())
                operator_queue.append(i)
            elif i in ['+', '-']:
                while True:
                    if len(operator_queue) == 0:
                        break
                    if operator_queue[-1] == '(':
                        break
                    expression_queue.append(operator_queue.pop())
                operator_queue.append(i)
            elif i == '(':
                operator_queue.append(i)
            elif i == ')':
                try:
                    while operator_queue[-1] != '(':
                        expression_queue.append(operator_queue.pop())
                    operator_queue.pop()
                except IndexError:
                    print('Invalid expression')
                    result = 'wrong'

    if len(operator_queue) != 0:
        if operator_queue[-1] not in ['+', '-', '*', '/']:
            print('Invalid expression')
            result = 'wrong'
        else:
            while True:
                if len(operator_queue) == 0:
                    break
                expression_queue.append(operator_queue.pop())

    if '(' in expression_queue:
        print('Invalid expression')
        result = 'wrong'

    if result == 'wrong':
        pass
    else:
        # print(expression_queue)
        return expression_queue


def calculation(expression_queue):
    result = ''
    result_queue = deque()
    while True:
        # print(expression_queue)
        # print(result_queue)
        if len(expression_queue) == 0:
            break
        element = expression_queue.popleft()
        if element.isdigit():
            if element == '0':
                result_queue.append(element)
            else:
                result_queue.append(int(element))

        elif element.isalpha():
            try:
                num = vars_stored[element]
                result_queue.append(num)
            except Exception:
                print('Unknown variable')
                result = 'wrong'
                break

        elif element == '+':
            try:
                x = result_queue.pop()
                y = result_queue.pop()
                r = y + x
                if r == 0:
                    result_queue.append('0')
                else:
                    result_queue.append(r)
            except Exception:
                print('Invalid expression')
                result = 'wrong'
                break

        elif element == '-':
            try:
                x = result_queue.pop()
                y = result_queue.pop()
                r = y - x
                if r == 0:
                    result_queue.append('0')
                else:
                    result_queue.append(r)

            except Exception:
                if len(expression_queue) == 0 and len(result_queue) == 0:
                    result_queue.append(x * -1)
                else:
                    print('Invalid expression')
                    result = 'wrong'
                    break

        elif element == '*':
            try:
                x = result_queue.pop()
                y = result_queue.pop()
                r = y * x
                result_queue.append(r)
            except Exception:
                print('Invalid expression')
                result = 'wrong'
                break

        elif element == '/':
            try:
                x = result_queue.pop()
                y = result_queue.pop()
                r = y / x
                result_queue.append(int(r))
            except Exception:
                print('Invalid expression')
                result = 'wrong'
                break

    if result == 'wrong':
        pass
    else:
        # print(result_queue)
        return result_queue.pop()


def main():

    while True:
        expression = input()

        # command check
        if expression.startswith(r'/'):
            command = command_check(expression)
            if command == 'exit':
                break
            elif command == 'help':
                continue
            elif command is None:
                print('Unknown command')
                continue

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
            post_expression = infix_to_postfix(expression)
            if post_expression:
                result = calculation(post_expression)
                if result:
                    print(result)


if __name__ == '__main__':
    vars_stored = dict()
    main()
