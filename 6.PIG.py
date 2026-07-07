import random

# ---------- Dice Roll Function ----------
def roll():
    return random.randint(1, 6)


# ---------- Number of Players ----------
while True:
    players = input("Enter the number of players (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Enter between 2 and 4 players.")
    else:
        print("Invalid input, try again.")


# ---------- Game Setup ----------
max_score = 50
player_scores = [0 for _ in range(players)]

print("\n🎲 Game Started 🎲\n")


# ---------- Game Loop ----------
while max(player_scores) < max_score:

    for player_index in range(players):

        print(f"\n👉 Player {player_index + 1}'s turn")
        print(f"Current Score: {player_scores[player_index]}")

        turn_score = 0

        while True:
            should_roll = input("Roll the dice? (y/n): ").lower()

            if should_roll == 'y':
                value = roll()
                print("You rolled:", value)

                if value == 1:
                    print("❌ You rolled 1 → Turn over, no points added.")
                    turn_score = 0
                    break
                else:
                    turn_score += value
                    print("Turn score:", turn_score)

            elif should_roll == 'n':
                print("You held your turn.")
                break

            else:
                print("Invalid input.")

        # Add turn score to total
        player_scores[player_index] += turn_score
        print(
            f"✅ Player {player_index + 1} Total Score:",
            player_scores[player_index]
        )

        # Check winner
        if player_scores[player_index] >= max_score:
            print(f"\n🏆 Player {player_index + 1} Wins the Game! 🏆")
            break

