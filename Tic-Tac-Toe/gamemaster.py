def tic_tac_toe(symbols):
    print('---------')
    all_move = list(symbols)
    first_line = ' '.join(all_move[:3])
    second_line = ' '.join(all_move[3:6])
    third_line = ' '.join(all_move[6:])
    print(f'| {first_line} |')
    print(f'| {second_line} |')
    print(f'| {third_line} |')
    print('---------')


tic_tac_toe(input('Enter cells: '))
