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
print()

# Receive Tax Rate and calculate the sales tax as also the total price (subtotal plus tax)
sales_tax_rate = int(input('What is the sales tax rate? '))
sales_tax = subtotal * (sales_tax_rate / 100)
total = subtotal + sales_tax

print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')
print()

# Receive the payment amount, calculate and display the change amount
payment_amount = float(input('What is the payment amount? '))
change_value = payment_amount - total

print(f'Change: ${change_value:.2f}')
