#!/usr/bin/env  python3

import random

def choose_word():
    words = ["cobra", "dancer", "mermaid", "batminton", "antidisestablishmentarianism", "supercalifragilisticexpialidocious"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    tries = 7

    while tries > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(f"\nCurrent word: {current_display}")
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                tries -= 1
            if set(guessed_letters) == set(secret_word):
                print(f"\nCongratulations! You guessed the word: {secret_word}")
                break
        else:
            print("Please enter a valid single letter.")

    if tries == 0:
        print(f"\nSorry, you ran out of tries. The correct word was: {secret_word}")

if __name__ == "__main__":
    hangman()

