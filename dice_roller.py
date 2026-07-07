import random

def roll_dice(sides):
    return random.randint(1, sides)

while True:
    try:
        sides = int(input("Enter the number of sides on the dice: "))
        if sides <= 0:
            print("Number of sides must be greater than 0.")
            continue
        result = roll_dice(sides)
        print(f"You rolled a {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    again = input("Roll again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break