class TicTacToe:

    def __init__(self):
        self.moves = 9
        self.straight = None
        self.move_list = ['O']
        self.new_ele_list = None
        self.coordinates = None
        self.row = None
        self.col = None
        self.occupied_cells = [[' ' for _i in range(3)] for _k in range(3)]
        self.over = ''

    def display(self):

        print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(self.new_ele_list[0][0], self.new_ele_list[0][1], self.new_ele_list[0][2],
                    self.new_ele_list[1][0], self.new_ele_list[1][1], self.new_ele_list[1][2],
                    self.new_ele_list[2][0], self.new_ele_list[2][1], self.new_ele_list[2][2]))

    def game_result(self):
        self.straight = [[self.new_ele_list[0][0], self.new_ele_list[0][1], self.new_ele_list[0][2]],
                        [self.new_ele_list[1][0], self.new_ele_list[1][1], self.new_ele_list[1][2]],
                        [self.new_ele_list[2][0], self.new_ele_list[2][1], self.new_ele_list[2][2]],
                        [self.new_ele_list[0][0], self.new_ele_list[1][0], self.new_ele_list[2][0]],
                        [self.new_ele_list[0][1], self.new_ele_list[1][1], self.new_ele_list[2][1]],
                        [self.new_ele_list[0][2], self.new_ele_list[1][2], self.new_ele_list[2][2]],
                        [self.new_ele_list[0][0], self.new_ele_list[1][1], self.new_ele_list[2][2]],
                        [self.new_ele_list[0][2], self.new_ele_list[1][1], self.new_ele_list[2][0]]]

        if any(i == ['X', 'X', 'X'] for i in self.straight):
            return 'X wins'
        if any(i == ['O', 'O', 'O'] for i in self.straight):
            return 'O wins'

    def enter_coordinates(self):
        print('''---------
|       |
|       |
|       |
---------''')

        while self.moves > 0:
            self.coordinates = input('Enter the coordinates: ')

            try:
                self.row, self.col = self.coordinates.split()
            except ValueError:
                print('You should enter numbers!')
                continue

            try:
                self.row = int(self.row)
                self.col = int(self.col)
            except ValueError:
                print('You should enter numbers!')
                continue

            if not 1 <= self.row <= 3 or not 1 <= self.col <= 3:
                print('Coordinates should be from 1 to 3!')
                continue

            if self.occupied_cells[self.row - 1][self.col - 1] != ' ':
                print('This cell is occupied! Choose another one!')
                continue

            else:
                if self.move_list[-1] == 'O':
                    self.occupied_cells[self.row - 1][self.col - 1] = 'X'
                    self.move_list.append('X')
                else:
                    self.occupied_cells[self.row - 1][self.col - 1] = 'O'
                    self.move_list.append('O')
                self.moves -= 1


# Left turn the matrix(occupied_cells) 1 time, then put into the matrix(new_ele_list)
#             self.new_ele_list = self.occupied_cells
            self.new_ele_list = [[], [], []]
            for row in self.occupied_cells:
                self.new_ele_list[2].append(row[0])
                self.new_ele_list[1].append(row[1])
                self.new_ele_list[0].append(row[2])

            self.display()

            if self.game_result() == 'X wins':
                self.over = 'over'
                print('X wins')
                break

            if self.game_result() == 'O wins':
                self.over = 'over'
                print('O wins')
                break

        if self.over != 'over':
            print('Draw')


game = TicTacToe()
game.enter_coordinates()
