def display(cells):
    line_1 = list(cells)[:3]
    line_2 = list(cells)[3:6]
    line_3 = list(cells)[6:]
    ele_list = [line_1, line_2, line_3]

    print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(ele_list[0][0], ele_list[0][1], ele_list[0][2],
                    ele_list[1][0], ele_list[1][1], ele_list[1][2],
                    ele_list[2][0], ele_list[2][1], ele_list[2][2]))

    return ele_list


def result_check():
    global elements
    ele_list = display(elements)
    x_win = 0
    o_win = 0
    straight = [(ele_list[0][0], ele_list[0][1], ele_list[0][2]),
                (ele_list[1][0], ele_list[1][1], ele_list[1][2]),
                (ele_list[2][0], ele_list[2][1], ele_list[2][2]),
                (ele_list[0][0], ele_list[1][0], ele_list[2][0]),
                (ele_list[0][1], ele_list[1][1], ele_list[2][1]),
                (ele_list[0][2], ele_list[1][2], ele_list[2][2]),
                (ele_list[0][0], ele_list[1][1], ele_list[2][2]),
                (ele_list[0][2], ele_list[1][1], ele_list[2][0])]
    for a, b, c in straight:
        if (a, b, c) == ('X', 'X', 'X'):
            x_win += 1
        elif (a, b, c) == ('O', 'O', 'O'):
            o_win += 1

    if x_win + o_win > 1:
        print('Impossible')

    elif abs(elements.count('X') - elements.count('O')) >= 2:
        print('Impossible')

    elif x_win == 1:
        print('X wins')

    elif o_win == 1:
        print('O wins')

    else:
        if elements.count('X') - elements.count('O') < 9:
            print('Game not finished')
        else:
            print('Draw')


def main():
    result_check()


if __name__ == '__main__':
    while True:
        elements = input('Enter cells: ').upper()
        if len(elements) != 9:
            print('Should be 9 letters')
            continue
        else:
            break
    main()


