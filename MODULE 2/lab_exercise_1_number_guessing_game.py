# Lab Exercise 1: Number Guessing Game
# The computer chooses a random number, and the user tries to guess it.

import random

secret_number = random.randint(1, 100)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("I have chosen a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempt(s).")
            break
    except ValueError:
        print("Please enter a valid whole number.")
