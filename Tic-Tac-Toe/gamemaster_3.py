class TicTacToe:
    elements_allow = ['X', 'O']

    def __init__(self):
        self.cells = None
        self.ele_list = []
        self.new_ele_list = []
        # self.board = [[' ' for _i in range(3)] for _k in range(3)]
        # self.move = 0
        self.coordinates = None
        self.row = None
        self.col = None
        self.occupied_cells = set()

    def display(self):

        for i in self.cells:
            if i in self.elements_allow:
                self.ele_list.append(i)
            else:
                self.ele_list.append(' ')

        self.new_ele_list = [self.ele_list[:3], self.ele_list[3:6], self.ele_list[6:]]
        print(self.new_ele_list)

        print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(self.new_ele_list[0][0], self.new_ele_list[0][1], self.new_ele_list[0][2],
                    self.new_ele_list[1][0], self.new_ele_list[1][1], self.new_ele_list[1][2],
                    self.new_ele_list[2][0], self.new_ele_list[2][1], self.new_ele_list[2][2]))

    def players_move(self):
        self.cells = input('Enter cells: ')
        self.display()

        while True:
            self.coordinates = input('Enter the coordinates: ')

            self.row, self.col = self.coordinates.split()

            try:
                self.row = int(self.row)
                self.col = int(self.col)
            except:
                print('You should enter numbers!')
                continue

            if not 1 <= self.row <= 3 or not 1 <= self.col <= 3:
                print('Coordinates should be from 1 to 3!')
                continue

            if (self.row, self.col) in self.occupied_cells:
                print('This cell is occupied! Choose another one!')
                continue

            self.occupied_cells.add((self.row, self.col))
            # self.new_ele_list[self.row - 1][self.col - 1] = 'X'
            break

        self.display()


game = TicTacToe()
game.players_move()









