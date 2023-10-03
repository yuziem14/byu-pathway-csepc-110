'''
Week 04 Team Activity Project: Guess My Number Game
CSEPC 110

Authors
@Yuri Nunes
@Gabriely Silveira
@Randy Munõz
'''

# Import random and os Library
import random
import os

MIN_NUMBER = 0
MAX_NUMBER = 100

keep_playing = True

while keep_playing:
    magic_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    # User guess will always start different from the magic number
    user_guess = magic_number + 1
    guess_tracker = 0

    while(magic_number != user_guess):
        user_guess = int(input('> What\'s the magic number? '))
        guess_tracker += 1

        if magic_number < user_guess:
            print('Lower')
        elif magic_number > user_guess:
            print('Higher')
        else:
            print('You guessed it!')
            print(f'Number Of Guesses: {guess_tracker}')
            print()

    keep_playing = input('> Play Again (Yes or No)? ').lower() == 'yes'

    # Clean the terminal after finishing the game
    os.system('cls' if os.name == 'nt' else 'clear')