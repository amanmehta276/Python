import random

print("🏹 Welcome to the Jungle Adventure Game 🏹")

name = input("Type your name: ")
health = 100
inventory = []

print(f"\nWelcome {name}! Your health is {health}.\n")

while True:

    answer = input(
        "You are on a dirt road. It ends here.\n"
        "You can go LEFT towards a river 🌊 or RIGHT towards a bridge 🌉.\n"
        "Type left/right: "
    ).lower()

    # ---------- LEFT PATH ----------
    if answer == "left":

        answer = input(
            "\nYou reach a river.\n"
            "Do you SWIM across or WALK around it?\n"
            "Type swim/walk: "
        ).lower()

        if answer == "swim":
            outcome = random.choice(["win", "lose"])

            if outcome == "lose":
                print("🐊 An alligator attacked you. Game Over.")
                health = 0
            else:
                print("💪 You swam safely and found a treasure chest!")
                inventory.append("Golden Coin")

        elif answer == "walk":
            print("🥵 You walked for miles and lost 30 health.")
            health -= 30

            if health <= 0:
                print("You collapsed. Game Over.")
            else:
                print(f"Health left: {health}")

        else:
            print("Invalid choice. You lost your way.")

    # ---------- RIGHT PATH ----------
    elif answer == "right":

        answer = input(
            "\nYou reach a wobbly bridge.\n"
            "Do you CROSS it or go BACK?\n"
            "Type cross/back: "
        ).lower()

        if answer == "cross":
            success = random.randint(1, 2)

            if success == 1:
                print("🌉 You crossed safely and found a sword!")
                inventory.append("Sword")
            else:
                print("You fell from the bridge. Game Over.")
                health = 0

        elif answer == "back":
            print("You went back and got lost in the jungle.")
            health -= 20

        else:
            print("Invalid option.")

    else:
        print("Invalid direction.")

    # ---------- CAVE EVENT ----------
    if health > 0:
        cave = input(
            "\nYou see a dark cave 🕳️.\n"
            "Do you ENTER or IGNORE it? (enter/ignore): "
        ).lower()

        if cave == "enter":
            if "Sword" in inventory:
                print("🗡️ You fought monsters and won the game! 🏆")
                break
            else:
                print("Monsters ate you. You needed a sword.")
                health = 0

        elif cave == "ignore":
            print("You move ahead safely.")

# ---------- HEALTH CHECK ----------
if health <= 0:
    print("\n💀 You died. Final Inventory:", inventory)
else:
    print(f"\n🎉 You won! Final Inventory: {inventory}")