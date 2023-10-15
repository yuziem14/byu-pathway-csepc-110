'''
@author Yuri Nunes

Week 05 Project: Shopping Cart

Exceed Requirement: Add quantity of items
'''

# Store Options ins Constants
ADD_ITEM = '1'
VIEW_CART = '2'
REMOVE_ITEM = '3'
COMPUTE_TOTAL = '4'
QUIT_PROGRAM = '5'
MENU_OPTIONS = [f'{ADD_ITEM}. Add item', f'{VIEW_CART}. View cart', f'{REMOVE_ITEM}. Remove item', f'{COMPUTE_TOTAL}. Compute total', f'{QUIT_PROGRAM}. Quit']

# Initialize Variables
selected_option = '0'
cart_items = []
prices = []
items_quantity = []

print('Welcome to the Shopping Cart Program!')

while(selected_option != QUIT_PROGRAM):
    print('Please select one of the following: ')
    for option in MENU_OPTIONS:
        print(option)

    selected_option = input('> Please enter an action: ')

    if(selected_option == ADD_ITEM):
        item_name = input('> What item would you like to add? ').lower()
        item_price = float(input(f'> What is the price of \'{item_name}\'? '))
        item_quantity = int(input(f'> What is the quantity of \'{item_name}\'? '))

        if(item_quantity < 1):
            print('Sorry. The quantity minimum is 1. If this is a mistake, please remove the item.')
            item_quantity = 1

        cart_items.append(item_name)
        prices.append(item_price)
        items_quantity.append(item_quantity)
        
        print(f'\'{item_name}\' has been added to the cart.')
    elif(selected_option == VIEW_CART):
        print('The contents of the shopping cart are:')

        for index in range(len(cart_items)):
            item_number = index + 1
            item_name = cart_items[index].capitalize()
            item_price = prices[index]
            item_quantity = items_quantity[index]
            total_price = item_price * item_quantity

            print(f'{item_number}. {item_name} - ${item_price:.2f} x {item_quantity} = ${total_price:.2f}')
    elif(selected_option == REMOVE_ITEM):
        item_number = int(input('> Which item would you like to remove? '))
        
        if(item_number < 1 or item_number > len(cart_items)):
            print('Sorry, that is not a valid item number.\n')
            continue

        index = item_number-1
        cart_items.pop(index)
        prices.pop(index)
        items_quantity.pop(index)
        print('Item removed.')
    elif(selected_option == COMPUTE_TOTAL):
        total_cart_price = 0
        for index in range(len(cart_items)):
            price = prices[index]
            item_quantity = items_quantity[index]
            total_cart_price += item_quantity * price
        
        print(f'The total price of the items in the shopping cart is ${total_cart_price:.2f}')
    elif(selected_option == QUIT_PROGRAM):
        print('Thank you. Goodbye.')
    else:
        print(f'The option {selected_option} is not available.')
    
    print()
