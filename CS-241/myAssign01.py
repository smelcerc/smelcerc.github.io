import random
from random import randint

print('Welcome to the number guessing game!')
seed = input('Enter random seed: ')

random.seed(seed)

keep_playing  = True

while keep_playing == True:

    num = randint(1,100)

    guesses = 1

    guessing = True

    while guessing == True:

        user_guess = int(input('\nPlease enter a guess: '))

        if user_guess > num:
            print('Lower')
        elif user_guess < num:
            print('Higher')
        else:
            print('Congratulations. You guessed it!')
            print(f'It took you {guesses} guesses.\n')
            guessing = False


        guesses += 1

    play_again = input('Would you like to play again (yes/no)? ')

    if play_again == 'yes':
        keep_playing = True
    else:
        keep_playing = False
    
print('Thank you. Goodbye.')