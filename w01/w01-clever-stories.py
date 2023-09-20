# The program asks for a user's friend name. In the end, the program challenge the user using the requested name data.

print('Please enter the following:\n')
story_adjective = input('adjective: ')
story_animal = input('animal: ')
story_verb = input('verb: ')
story_exclamation = input('exclamation: ')
story_verb1 = input('verb: ')
story_verb2 = input('verb: ')
friend_name = input('close friend name: ').capitalize()

print('\nYour story is:\n\n')
print(f'The other day, I was really in trouble. It all started when I saw a very {story_adjective} {story_animal} {story_verb} down the hallway.')
print(f'"{story_exclamation.capitalize()}!" I yelled. But all I could think to do was to {story_verb1} over and over. Miraculously, that caused it to stop, but not before it tried to {story_verb2} right in front of my family.')
print(f'Share this story with {friend_name} and let\'s see if believes in you! Have fun!')