from termcolor import colored
import random
import sys

def read_random_word():
    with open("words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)

print("Let's play Wordle:")
print("Type a 5 letter word below and press Enter. You have 6 tries to guess the random word.\n")

word = read_random_word()

for attempt in range(1,7):
    guess = input().lower()
    
    # overwrite the last line in the console
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

    # print colored letters
    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(guess[i], end="")
    print()
    
    if guess == word:
        print("Congratulations! You guessed the word in %i guesses." %attempt)
    elif attempt == 6:
        print("You didn't guess the word within 6 tries, it was '%s'" %word)
