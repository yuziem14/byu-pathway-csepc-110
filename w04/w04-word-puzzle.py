'''
@author Yuri Nunes

Week 04 Project: Word Puzzle Game

Exceed Requirement: None
'''

ERROR_MESSAGE = '> Sorry, the guess must have the same number of letters as the secret word.'

# Store the secret word
secret = 'temple'
hint = '______'
guess = ''
number_guesses = 0

print('Welcome to the world guessing game!')

while secret != guess:
    new_hint = ''
    number_guesses += 1

    print(f'Your hint is: {hint}')
    guess = input('> What is your guess? ')

    if len(secret) != len(guess):
        print(ERROR_MESSAGE)
        continue

    for index in range(0, len(secret)):
        secret_letter = secret[index]
        guess_letter = guess[index]

        letter_index = secret.find(guess_letter, 0, len(secret))

        if(letter_index >= 0):
            new_hint += guess_letter.upper() if guess_letter == secret_letter else guess_letter
        else:
            new_hint += '_'
        
        hint = new_hint