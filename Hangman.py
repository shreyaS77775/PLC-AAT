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

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("\nEnter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid input\n")
            continue

        if guess in guessed_letters:
            print(f"\n{guess} is already guessed.\n")
            continue

        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\nYOU WIN!!\n")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\nYOU LOSE!!\n")
            is_running = False

if __name__ == "__main__":
    main()
        

