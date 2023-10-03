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
os.system('cls' if os.name == 'nt' else 'clear')

user_number = int(input('> What\'s the magic number? '))

if user_number < magic_number:
    print('Lower')
elif user_number > magic_number:
    print('Higher')
else:
    print('You guessed it!')