'''
Week 04 Team Activity Project: Guess My Number Game
CSEPC 110

Authors
@Yuri Nunes
@Gabriely Silveira
@Randy Munõz
'''

# Import OS and Random Library
import os
import random


magic_number = int(input('> What is the magic number to guess? '))
# User guess will always start different from the magic number
user_guess = magic_number + 1

os.system('cls' if os.name == 'nt' else 'clear')

while(magic_number != user_guess):
    user_guess = int(input('> What\'s the magic number? '))

    if user_guess < magic_number:
        print('Lower')
    elif user_guess > magic_number:
        print('Higher')
    else:
        print('You guessed it!')
