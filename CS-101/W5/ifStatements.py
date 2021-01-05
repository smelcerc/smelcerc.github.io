first_number = float(input('What is the first number? '))
second_number = float(input('What is the second number? '))

if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')

if first_number == second_number:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if first_number < second_number:
    print('The second number is greater')
else:
    print('The second number is not greater')

programmers_favorite_animal = "dog"
users_favorite_animal = input('\nWhat is your favorite animal? ')

if users_favorite_animal.lower() == programmers_favorite_animal.lower():
    print("That's my favorite animal too!")
else: 
    print("That one is not my favorite.")