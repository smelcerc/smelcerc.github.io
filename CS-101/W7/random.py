import random

play = "yes"

while play == "yes":
    number = random.randrange(0, 100)

    guesses = 0

    guess = -1

    while guess != number:
        guess = int(input("What is your guess? "))
        guesses = guesses + 1

        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print("You guessed it!")

    print(f"You guessed it in {guesses} tries")

    play = input("Do you want to play again (yes/no)? ")

