import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice — please type rock, paper, or scissors (or Q to quit).")
        continue

    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1
    again=input("Enter 1 if wanna play else any diigt: ")

    if again!="1":
        print("Thanks for playing")
        break
    
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Good Bye!")