import random
import getpass

def guesser():
    print("Welcome to the game")

    players=[]
    n=int(input("Enter the number of players:"))
    for i in range(n):
        n_name=input(f"\nEnter the name of player {i+1}: ",)
        players.append(n_name)

    print("\nChoose who will be the chooser,")
    chooser=input("Enter the name of the chosoer: ")

    if chooser not in players:
        print("Invalid player name! Restart the game.")
        return

    
    print(f"\n {chooser} will now guess a number to guess for others! ")
    try:
        chooser_guess=int(getpass.getpass("enter the secret number to guess."))
    except ValueError:
        print("Invalid number,Please enter a valid one")
        return
    
    max_chance=3
    chance=0
    winner=[]

    while chance<max_chance:
        guesses=[]
        print(f"--Round:{chance+1}--")

        for player in players:
            if player != chooser:
                try:
                    players_guess=int(input(f"{player},enter your guess: "))
                except ValueError:
                    print("Invalid input!,Enter a valid number")
                    players_guess=None
                guesses.append((player,players_guess))
    
        for player,players_guess in guesses:
            if players_guess==chooser_guess:
                winner.append(player)
        if winner:
            print(f"Congratulations {player} your guess,{players_guess} is correct.")
            return 
        print("\n No correct guesss,move to next round")
        chance+=1

    if not winner:
        print(f"\n Game over,No one guessed it,right number is {chooser_guess}")
        print(f"{chooser} won the game")
    else:
            print(f"\ Congratulatios to the winners: {','.join(winner)}")

    print("Thanks for playing")


guesser()

# a=getpass.getpass()
# print(a)