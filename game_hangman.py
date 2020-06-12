import random


class GangMan:
    words = ['python', 'java', 'kotlin', 'javascript']

    def __init__(self):
        self.word = random.choice(GangMan.words)
        self.result = '-' * len(self.word)
        self.lst = list(self.result)
        self.guess_words = set()
        self.status = 'on'
        self.time = None
        self.action = ''

    def guess(self, time):
        self.time = time

        while self.time > 0:
            if self.result == self.word:
                self.status = 'off'
                break

            print()
            print(self.result)
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print('You should input a single letter')
                continue

            elif not letter.islower():
                print('It is not an ASCII lowercase letter')
                continue

            elif letter in self.guess_words:
                print('You already typed this letter')
                continue

            elif letter not in set(self.word):
                print('No such letter in the word')
                self.time -= 1
                self.guess_words.add(letter)

            else:
                count = 0
                for l in self.word:
                    if letter == l:
                        self.lst[count] = letter
                    count += 1
                self.result = ''.join(self.lst)
                self.guess_words.add(letter)

        if self.status == 'off':
            print('\nYou guessed the word!\nYou survived!\n\n')
        else:
            print('\nYou are hanged!\n\n')

    def play(self):
        while True:
            self.action = input('Type "play" to play the game, "exit" to quit: ')
            if self.action == 'exit':
                break
            elif self.action == 'play':
                game_start.guess(8)
            else:
                continue


# Game start
print('H A N G M A N')
game_start = GangMan()
game_start.play()
