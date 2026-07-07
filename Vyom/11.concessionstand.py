# Concession stand program

# Concession Stand Program

menu = {
    "pizza": 120,
    "burger": 80,
    "popcorn": 60,
    "fries": 70,
    "coke": 40
}

cart = []
total = 0

print("------ MENU ------")
for item, price in menu.items():
    print(f"{item:10}: ₹{price}")
print("------------------")

while True:
    food = input("Select an item (q to quit): ").lower()

    if food == "q":
        break

    if food in menu:
        cart.append(food)
        print(f"{food} added to cart.")
    else:
        print("Item not available.")

print("\n------ YOUR ORDER ------")
for food in cart:
    total += menu[food]
    print(food)

print(f"\nYour total is: ₹{total}")