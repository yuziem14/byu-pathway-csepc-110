'''
@author Yuri Nunes

Week 04 Project: Word Puzzle Game

Exceed Requirement:
'''

ERROR_MESSAGE = '> Sorry, the guess must have the same number of letters as the secret word.'

# Store the secret word
secret = 'lamanites'
guess = ''
number_guesses = 0

print('Welcome to the world guessing game!')

while secret != guess:
    guess = input('> What is your guess? ')

    if len(secret) != len(guess):
        print(ERROR_MESSAGE)
        continue

    number_guesses += 1

    if(guess == secret):
        print('Congratulations! You guessed it!')
        print(f'It took you {number_guesses} guesses.')