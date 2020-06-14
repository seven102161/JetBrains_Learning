class TicTacToe:
    elements_allow = ['X', 'O']

    def __init__(self):
        self.elements_allow = TicTacToe.elements_allow
        self.cells = None
        self.count_x = 0
        self.count_y = 0
        self.ele_list = []
        self.new_ele_list = []
        self.straight = []
        self.winner = []
        self.status = 'on'

    def game_display(self, cells):

        for i in cells:
            if i in self.elements_allow:
                self.ele_list.append(i)
                if i == 'X':
                    self.count_x += 1
                else:
                    self.count_y += 1
            else:
                self.ele_list.append(' ')

        self.new_ele_list = [self.ele_list[:3], self.ele_list[3:6], self.ele_list[6:]]

        print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(self.new_ele_list[0][0], self.new_ele_list[0][1], self.new_ele_list[0][2],
                            self.new_ele_list[1][0], self.new_ele_list[1][1], self.new_ele_list[1][2],
                            self.new_ele_list[2][0], self.new_ele_list[2][1], self.new_ele_list[2][2]))
        print(self.game_result())

    def game_result(self):
        self.straight = [[self.new_ele_list[0][0], self.new_ele_list[0][1], self.new_ele_list[0][2]],
                        [self.new_ele_list[1][0], self.new_ele_list[1][1], self.new_ele_list[1][2]],
                        [self.new_ele_list[2][0], self.new_ele_list[2][1], self.new_ele_list[2][2]],
                        [self.new_ele_list[0][0], self.new_ele_list[1][0], self.new_ele_list[2][0]],
                        [self.new_ele_list[0][1], self.new_ele_list[1][1], self.new_ele_list[2][1]],
                        [self.new_ele_list[0][2], self.new_ele_list[1][2], self.new_ele_list[2][2]],
                        [self.new_ele_list[0][0], self.new_ele_list[1][1], self.new_ele_list[2][2]],
                        [self.new_ele_list[0][2], self.new_ele_list[1][1], self.new_ele_list[2][0]]]

        for line in self.straight:
            count_x = 0
            count_y = 0
            for i in line:
                if i == 'X':
                    count_x += 1
                elif i == 'O':
                    count_y += 1
            if count_x == 3:
                self.winner.append('X')
            elif count_y == 3:
                self.winner.append('O')

        while self.status != 'off':
            if len(self.winner) > 1:
                self.status = 'off'
                return 'Impossible'

            if abs(self.count_x - self.count_y) >1:
                self.status = 'off'
                return 'Impossible'

            if self.count_x + self.count_y < 9:
                self.status = 'off'
                if len(self.winner) != 0:
                    if self.winner[0] == 'X':
                        self.status = 'off'
                        return 'X wins'
                    elif self.winner[0] == 'O':
                        self.status = 'off'
                        return 'O wins'
                else:
                    return 'Game not finished'

            else:
                self.status = 'off'
                if len(self.winner) == 0:
                    self.status = 'off'
                    return 'Draw'
                elif self.winner[0] == 'X':
                    self.status = 'off'
                    return 'X wins'
                elif self.winner[0] == 'O':
                    self.status = 'off'
                    return 'O wins'


game_start = TicTacToe()
game_start.game_display(input('Enter cells: ').upper())