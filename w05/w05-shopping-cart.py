'''
@author Yuri Nunes

Week 05 Project: Shopping Cart

Exceed Requirement: None
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
cart = []

print('Welcome to the Shopping Cart Program!')

while(selected_option != QUIT_PROGRAM):
    print('Please select one of the following: ')
    for option in MENU_OPTIONS:
        print(option)

    selected_option = input('> Please enter an action: ')

    if(selected_option == ADD_ITEM):
        item_name = input('> What item would you like to add? ').lower()
        print(f'\'{item_name}\' has been added to the cart.')
        cart.append(item_name)
    elif(selected_option == VIEW_CART):
        print('The contents of the shopping cart are:')
        for index in range(len(cart)):
            print(f'{index+1}. {cart[index].capitalize()}')
    elif(selected_option == REMOVE_ITEM):
        print()
    elif(selected_option == COMPUTE_TOTAL):
        print()
    elif(selected_option == QUIT_PROGRAM):
        print('Thank you. Goodbye.')
    else:
        print(f'The option {selected_option} is not available.')
    
    print()
