'''
@author Yuri Nunes

Week 04 Project: Word Puzzle Game

Exceed Requirement: Get a random secret of a list of secrets and use colors to make game more fun
'''
# Import random module and OS module for clear console
import os
import random

# Declare ANSI Colors Constants
BOLD = "\u001b[1m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
GREEN_BOLD = "\033[1;32m"
PURPLE_BOLD = "\033[1;35m"
RESET_COLOR = "\u001b[0m"

# Declare all the game messages
ERROR_MESSAGE = f'{RED}> Sorry, the guess must have the same number of letters as the secret word.{RESET_COLOR}'
CONGRATULATIONS_MESSAGE = f'{GREEN_BOLD}Congratulations! You guessed it!{RESET_COLOR}'
TOTAL_GUESSES_MESSAGE = f'{GREEN_BOLD}It took you [number_guesses] guesses.{RESET_COLOR}'
HINT_MESSAGE = f'{GREEN}Your hint is: [hint]{RESET_COLOR}'
GUESS_QUESTION = f'{BOLD}> What is your guess?{RESET_COLOR} '


# Initialize a list of secret
secret_list = ['temple', 'mosiah', 'lamanites', 'moroni', 'alma', 'nephi']
# Store the secret word get random and initialize other variables
secret = secret_list[random.randint(0, len(secret_list)-1)]
secret_length = len(secret)
hint = '______'
guess = ''
number_guesses = 0

print(f'{PURPLE_BOLD}Welcome to the world guessing game!{RESET_COLOR}')

while secret != guess:    
    new_hint = ''
    number_guesses += 1
    
    # Check if hint should be displayed. If its the first guess display anyway
    throw_error = secret_length != len(guess) if number_guesses != 1 else False

    if throw_error == False:
        print(HINT_MESSAGE.replace('[hint]', hint))

    guess = input(GUESS_QUESTION).lower()

    throw_error = secret_length != len(guess)

    # If there's error display message and restart the loop
    if throw_error:
        print(ERROR_MESSAGE)
        continue
    
    for index in range(0, secret_length):
        secret_letter = secret[index]
        guess_letter = guess[index]

        # Check if the letter is in the secret. Returns -1 if not.
        letter_index = secret.find(guess_letter, 0, secret_length)

        # If exists returns uppercase letter if the secret and guess letter are the same.
        if(letter_index >= 0):
            letter_to_add = f'{GREEN_BOLD}{guess_letter.upper()}{GREEN}'
            new_hint += letter_to_add if guess_letter == secret_letter else guess_letter
        else:
            new_hint += '_'
        
        hint = new_hint
    
    if(secret != guess):
        print(RESET_COLOR)
        os.system('cls' if os.name=='nt' else 'clear')

print(CONGRATULATIONS_MESSAGE)
print(TOTAL_GUESSES_MESSAGE.replace('[number_guesses]', str(number_guesses)))