class TicTacToe:
    elements_allow = ['X', 'O']

    def __init__(self):
        self.cells = None
        self.ele_list = []
        self.new_ele_list = []
        self.coordinates = None
        self.row = None
        self.col = None
        self.occupied_cells = [[], [], []]

    def display(self):

        print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(self.new_ele_list[0][0], self.new_ele_list[0][1], self.new_ele_list[0][2],
                    self.new_ele_list[1][0], self.new_ele_list[1][1], self.new_ele_list[1][2],
                    self.new_ele_list[2][0], self.new_ele_list[2][1], self.new_ele_list[2][2]))

    def enter_cells(self):
        self.cells = input('Enter cells: ')
        for i in self.cells:
            if i in self.elements_allow:
                self.ele_list.append(i)
            else:
                self.ele_list.append(' ')

        self.new_ele_list = [self.ele_list[:3], self.ele_list[3:6], self.ele_list[6:]]
        self.display()

    def enter_coordinates(self):
        temp_list_1 = [[], [], []]
        temp_list_2 = [[], [], []]

# Left turn the matrix(new_ele_list) 3 times

        for row in self.new_ele_list:
            temp_list_1[2].append(row[0])
            temp_list_1[1].append(row[1])
            temp_list_1[0].append(row[2])

        for row in temp_list_1:
            temp_list_2[2].append(row[0])
            temp_list_2[1].append(row[1])
            temp_list_2[0].append(row[2])

        for row in temp_list_2:
            self.occupied_cells[2].append(row[0])
            self.occupied_cells[1].append(row[1])
            self.occupied_cells[0].append(row[2])

        while True:
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
                self.occupied_cells[self.row - 1][self.col - 1] = 'X'
                break

# Left turn the matrix(occupied_cells) 1 time, then put into the matrix(new_ele_list)
        self.new_ele_list = [[], [], []]
        for row in self.occupied_cells:
            self.new_ele_list[2].append(row[0])
            self.new_ele_list[1].append(row[1])
            self.new_ele_list[0].append(row[2])

        self.display()


game = TicTacToe()
game.enter_cells()
game.enter_coordinates()
