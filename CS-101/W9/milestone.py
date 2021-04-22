print("Welcome to the Shopping Cart Program!")

menu_list = ['Add item', 'View cart', 'Remove item', 'Compute total', 'Quit']
action_menu = ''
item_number = 0

for item in menu_list:
    item_string = f'{item_number + 1}. {item}\n'
    item_number = item_number + 1
    action_menu = action_menu + item_string

action_menu_prompt = f'Please select one of the following: \n{action_menu}' 

action_selection = ''

cart = {}

while action_selection != '5':
    print(action_menu_prompt)
    action_selection = input('Please enter an action: ')
    #Add item to the cart
    if action_selection == '1' or action_selection == 'Add item':
        item = input('What item would you like to add? ')
        price = float(input(f"What is the price of '{item}'? "))
        cart[item] = price
        print(f"'{item}' has been added to the cart.\n")

    #View cart items
    elif action_selection == '2' or action_selection == 'View cart':
        print('The contents of the shopping cart are:')
        item_order = 0
        for item in cart:
            print(f'{item_order + 1}. {item} - ${cart[item]:.2f}')
            item_order = item_order + 1
        print()

    #Remove items from the cart
    elif action_selection == '3' or action_selection == 'Remove item':
        item_remove = int(input("Which item would you like to remove? "))
        iter = 0
        for key in cart:
            if item_remove > len(cart):
                print(f'There are only {len(cart)} items in the cart. Please enter a valid option.')
                break
            if iter == (item_remove - 1):
                del cart[key]
                print(f'{key} removed.\n')
                break
            iter = iter + 1

    #Compute the total of the cart
    elif action_selection == '4' or action_selection == 'Compute total':
        total = 0
        if len(cart) > 0:
            for key in cart:
                total += cart.get(key)
        print(f'The total price of the items in the shopping cart is: ${total:.2f}\n')
    
    #Quit the cart
    elif action_selection == '5' or action_selection == 'Quit':
        print('Quit')
        break
    else:
        print('Please select an option listed above...')

print('Thank you, Goodbye.')