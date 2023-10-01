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
FIGHT_ACTION = 'FIGHT'
WAIT_ACTION = 'WAIT'
GOING_ACTION = 'GOING'
STOP_ACTION = 'STOP'
APOLOGIZE_ACTION = 'APOLOGIZE'
ACCEPT_ACTION = 'ACCEPT'
RECOVER_ACTION = 'RECOVER'
LOSING_ACTION = 'LOSING'
BETRAY_ACTION = 'BETRAY'

# Initializes story sentences constants
ERROR_SENTENCE = 'This action is not availabe.'
INITIAL_SENTENCE = f'> You\'re a soldier in World War II. You see your companion on the ground, injured. Do you {BOLD}{HELP_ACTION}{END_BOLD} him or let him {BOLD}{DIE_ACTION}{END_BOLD}? '
HELP_ACTION_SENTENCE = f'> While you run in his direction, an enemy hurls a grenade your way. Do you {BOLD}{THROW_ACTION}{END_BOLD} the grenade in another direction or {BOLD}{RUN_ACTION}{END_BOLD} to a different one? '
DIE_ACTION_SENTENCE = f'> Your companion has died, and he held an important secret that is now in the hands of the enemy. Do you plan to {BOLD}{REPORT_ACTION}{END_BOLD} it to your superiors or {BOLD}{HIDE_ACTION}{END_BOLD} this fact? '
THROW_ACTION_SENTENCE = f'> You threw the grenade into the enemy crowd, defeating them, and then dove for cover beside your companion. In this critical moment, you called for medical support. While you waited for them to arrive, did you decide to {BOLD}{FIGHT_ACTION}{END_BOLD} the other enemies or {BOLD}{WAIT_ACTION}{END_BOLD} for medical assistance? '
RUN_ACTION_SENTENCE = f'> When you ran in a different direction, you were shot in the leg, and now you are struggling to reach your companion. What will you do? Will you keep {BOLD}{GOING_ACTION}{END_BOLD} or {BOLD}{STOP_ACTION}{END_BOLD}? '
REPORT_ACTION_SENTENCE = f'> Reporting that you left your companion is considered a betrayal of the nation and an abandonment of your mission. Will you try to {BOLD}{APOLOGIZE_ACTION}{END_BOLD} for your mistake, {BOLD}{ACCEPT_ACTION}{END_BOLD} the decision, or {BOLD}{BETRAY_ACTION}{END_BOLD} everyone? '
HIDE_ACTION_SENTENCE = f'> By hiding this important information, you risk losing the war. Will you attempt to {BOLD}{RECOVER_ACTION}{END_BOLD} the secret or accept the possibility of {BOLD}{LOSING_ACTION}{END_BOLD} the war? '
FIGHT_ACTION_SENTENCE = f'> After fighting, you manage to defeat the enemies, and your companion is safe. Among the enemies, you find one who possesses a crucial strategy to win the war. You deliver this strategy to your leader, and they formulate a counter-strategy that ultimately leads to victory in the war.'
WAIT_ACTION_SENTENCE = f'> While waiting for medical assistance, a large number of enemies close in on your position. It\'s apparent that survival is unlikely, so you make the difficult choice to destroy the secret your companion carries with him. After a few seconds, both you and your companion succumb to your injuries, but due to your actions, the enemy is prevented from winning the war for the time being.'
GOING_ACTION_SENTENCE = f'> With tremendous effort, you manage to reach your companion in time, but sadly, he succumbs to his injuries and passes away. However, another soldier comes to your rescue, and together, you retrieve your fallen comrade. The secret remains safe, but the war is far from over. At the very least, you have ensured that your friend has an honorable death.'
STOP_ACTION_SENTENCE = f'> A soldier never gives up. You have many choices, but you weren\'t prepared for battlefield. You died and will never know if your army won the war.'
APOLOGIZE_ACTION_SENTENCE = f'> You apologize for your mistake and offer yourself as a sacrifice. As an explosives expert, you had already planted numerous bombs in the enemy\'s field, which resulted in the deaths of many of them and brought your army closer to victory, but you died in the process. This act becomes your redemption.'
ACCEPT_ACTION_SENTENCE = f'> You accept it and return home without honor. A few months later, your country loses the war because of the secret you lost. You know it\'s your fault.'
RECOVER_ACTION_SENTENCE = f'> In the process of recovering the secret, you become a spy. You manipulate the enemies by distorting the secret, leading them to adopt the wrong strategy, and as a result, they are defeated. Victory is yours.'
LOSING_ACTION_SENTENCE = f'> The secret they obtained was that all the food and supplies would arrive in a week at 9 AM on the coast near the main headquarters. The enemies destroyed all the food and supplies, and after two days, they launched an invasion, resulting in the deaths of all the soldiers. You have lost!'
BETRAY_ACTION_SENTENCE = f'> You kill everyone, including yourself, and let the enemies win the war.'

# Game

print('Welcome to the adventure game! Remember to choose one of the actions in bold.')
print()

next_action = input(INITIAL_SENTENCE).upper()
show_error_message = False

if next_action == HELP_ACTION:
    next_action = input(HELP_ACTION_SENTENCE).upper()

    if next_action == THROW_ACTION:
        next_action = input(THROW_ACTION_SENTENCE).upper()
        if next_action == FIGHT_ACTION:
            print(FIGHT_ACTION_SENTENCE)
        elif next_action == WAIT_ACTION:
            print(WAIT_ACTION_SENTENCE)
        else:
            show_error_message = True
            
    elif next_action == RUN_ACTION:
        next_action = input(RUN_ACTION_SENTENCE).upper()
        if next_action == GOING_ACTION:
            print(GOING_ACTION_SENTENCE)
        elif next_action == STOP_ACTION:
            print(STOP_ACTION_SENTENCE)
        else:
            show_error_message = True
    else:
        show_error_message = True

elif next_action == DIE_ACTION:
    next_action = input(DIE_ACTION_SENTENCE).upper()

    if next_action == REPORT_ACTION:
        next_action = input(REPORT_ACTION_SENTENCE).upper()
        if next_action == APOLOGIZE_ACTION:
            print(APOLOGIZE_ACTION_SENTENCE)
        elif next_action == ACCEPT_ACTION:
            print(ACCEPT_ACTION_SENTENCE)
        elif next_action == BETRAY_ACTION:
            print(BETRAY_ACTION_SENTENCE)
        else:
            show_error_message = True
            
    elif next_action == HIDE_ACTION:
        next_action = input(HIDE_ACTION_SENTENCE).upper()
        if next_action == RECOVER_ACTION:
            print(RECOVER_ACTION_SENTENCE)
        elif next_action == LOSING_ACTION:
            print(LOSING_ACTION_SENTENCE)
        else:
            show_error_message = True
    else:
        show_error_message = True
else:
    show_error_message = True

if show_error_message:
    print(ERROR_SENTENCE)