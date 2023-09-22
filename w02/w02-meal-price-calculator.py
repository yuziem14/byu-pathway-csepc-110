'''
@author Yuri Nunes

Week 02 Project: Meal Price Calculator

Exceed Requirement: Ask the user if he wants to give a tip and calculate the total that must be paid and the change
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
total_price = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
print(f'Subtotal: ${total_price:.2f}')
print()

# Receive Tax Rate and calculate the sales tax, add the sales tax with the subtotal and display it
sales_tax_rate = int(input('What is the sales tax rate? '))
sales_tax = total_price * (sales_tax_rate / 100)
total_price += sales_tax

print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Subtotal: ${total_price:.2f}')
print()

# Ask if the user wants to give a tip and add to the subtotal
tip_value = float(input('How much you want to give for tip? (if none, type 0) '))
total_price += tip_value
print(f'Total: ${total_price:.2f}')
print()

# Receive the payment amount, calculate and display the change amount
payment_amount = float(input('What is the payment amount? '))
change_value = payment_amount - total_price

print(f'Change: ${change_value:.2f}')
