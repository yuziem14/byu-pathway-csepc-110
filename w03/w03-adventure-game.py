'''
@author Yuri Nunes

Week 03 Project: Adventure Game

Exceed Requirement: On the HELP > RUN > STOP choice its make an trick saying that because of wrong choices the user will never know the ending.
'''

# Set special format strings
BOLD = '\033[1m'
END_BOLD = '\033[0m'

# Set the actions strings
HELP_ACTION = 'HELP'
DIE_ACTION = 'DIE'
THROW_ACTION = 'THROW'
RUN_ACTION = 'RUN'
REPORT_ACTION = 'REPORT'
HIDE_ACTION = 'HIDE'

# Initializes story sentences constants
ERROR_SENTENCE = 'This action is not availabe.'
INITIAL_SENTENCE = f'You\'re a soldier in World War II. You see your companion on the ground, injured. Do you {BOLD}{HELP_ACTION}{END_BOLD} him or let him {BOLD}{DIE_ACTION}{END_BOLD}? '
HELP_ACTION_SENTENCE = f'While you run in his direction, an enemy hurls a grenade your way. Do you {BOLD}{THROW_ACTION}{END_BOLD} the grenade in another direction or {BOLD}{RUN_ACTION}{END_BOLD} to a different one? '
DIE_ACTION_SENTENCE = f'Your companion has died, and he held an important secret that is now in the hands of the enemy. Do you plan to {BOLD}{REPORT_ACTION}{END_BOLD} it to your superiors or {BOLD}{HIDE_ACTION}{END_BOLD} this fact? '

print('Welcome to the adventure game! Remember to choose one of the actions in bold.')
print()

next_action = input(INITIAL_SENTENCE).upper()

if next_action == HELP_ACTION:
    next_action = input(HELP_ACTION_SENTENCE).upper()
elif next_action == DIE_ACTION:
    next_action = input(DIE_ACTION_SENTENCE).upper()
else:
    print(ERROR_SENTENCE)


