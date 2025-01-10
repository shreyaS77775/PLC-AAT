#Hangman Game in Python

from wordslist import words
import random

hangman_art = {
    0: ("     ",
        "     ",
        "     "),
    1: ("  O  ",
        "     ",
        "     "),
    2: ("  O  ",
        "  |  ",
        "     "),
    3: ("  O  ",
        " /|  ",
        "     "),
    4: ("  O  ",
        " /|\\",
        "     "),
    5: ("  O  ",
        " /|\\",
        " /   "),
    6: ("  O  ",
        " /|\\",
        " / \\")
}

def display_man(wrong_guesses):
    print("*********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*********")
    
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
    

