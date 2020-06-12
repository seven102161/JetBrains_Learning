"""
Game: Simon says
Do you know the game "Simon says"?
The instructor, "Simon", says what the players should do, e.g. "jump in the air" or "close your eyes".
The players should follow the instructions only if the phrase starts with or end with "Simon says",
If it starts or ends with the words "Simon says", the players say: "I + (what you would do)!"
Otherwise, the players say: "I won't do it!".

This is a practice to use "find" function and slice a string.
"""


def what_to_do(instructions):
    instructions = instructions.rstrip()
    key_words = 'Simon says'

    if instructions.startswith(key_words):
        ind = len(key_words)
        action_do = instructions[ind + 1:]
        return 'I {}!'.format(action_do)

    if instructions.endswith(key_words):
        ind = instructions.find(key_words)
        action_do = instructions[:ind - 1]
        return 'I {}!'.format(action_do)

    return "I won't do it!"


do = input()  # Say what your instruction is?
what_to_do(do)
