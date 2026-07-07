# Number guessing game

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("🎮 Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")

        elif guess < answer:
            print("Too low! Try again.")

        elif guess > answer:
            print("Too high! Try again.")

        else:
            print(f"🎉 Correct! The number was {answer}")
            print(f"You guessed it in {guesses} attempts.")
            is_running = False

    else:
        print("Please enter a valid number.")