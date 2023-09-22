'''
@author Yuri Nunes

Week 02 Project: Meal Price Calculator
'''

print('Let\'s calculate the price of your meal. Answer the following:')
print()

# Receiving Data For The User
child_meal_price = float(input('What is the price of a child\'s meal? '))
adult_meal_price = float(input('What is the price of a adult\'s meal? '))
number_of_children = int(input('How many children are there? '))
number_of_adults = int(input('How many adults are there? '))
print()

# Calculate Sub Total
subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
print(f'Subtotal: ${subtotal:.2f}')
