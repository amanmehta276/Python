# Python slot machine
import random

def spin_row():
    symbols = ["🍒", "🍉", "🥭", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))


def pay_out(row, bet):
    # Jackpot: all 3 symbols match
    if row[0] == row[1] == row[2]:
        print("🎉 JACKPOT! 🎉")
        return bet * 10

    # Small win: any 2 symbols match
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print("😊 Two symbols matched!")
        return bet * 2

    # No win
    else:
        print("😢 No match!")
        return 0


def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🥭 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"\nCurrent balance: ${balance}")

        bet = input("Place your bet amount: $")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        if bet > balance:
            print("Insufficient funds.")
            continue

        balance -= bet

        # Spin and display row
        row = spin_row()
        print("\nSpinning...\n")
        print_row(row)

        # Calculate winnings
        winnings = pay_out(row, bet)
        balance += winnings

        print(f"You won: ${winnings}")
        print(f"Current balance: ${balance}")

        # Ask to continue
        play_again = input("\nPlay again? (y/n): ").lower()

        if play_again != "y":
            break

    print(f"\nGame over! Final balance: ${balance}")


if __name__ == "__main__":
    main()