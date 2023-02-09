print("Guess the Number Game")

print("---------------------")

print("Guess a number between 1 and 100: ")

import random

number = random.randint(1, 100)

guess = None

while guess != number:

    guess = int(input("Your guess: "))

    

    if guess < number:

        print("Too low, try again")

    elif guess > number:

        print("Too high, try again")

    else:

        print("You won! The number was", number)

