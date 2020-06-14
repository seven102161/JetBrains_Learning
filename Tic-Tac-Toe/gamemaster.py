def tic_tac_toe(cells):
    elements_allow = ['X', 'O', '_']

    while True:
        elements = list(cells)
        if len(elements) != 9:
            print('should be 9 elements')
            continue

        else:
            for i in elements:
                if i not in elements_allow:
                    print('Not legal element')
                    continue


            first_line = ' '.join(elements[:3])
            second_line = ' '.join(elements[3:6])
            third_line = ' '.join(elements[6:])

            print('---------')
            print(f'| {first_line} |')
            print(f'| {second_line} |')
            print(f'| {third_line} |')
            print('---------')

            break


tic_tac_toe(input('Enter cells: '))
