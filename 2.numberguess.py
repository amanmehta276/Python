import random
top_of_range=input("Type a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

chance=0


guess=random.randint(0,top_of_range)

while True:
    chance+=1

    choice=input("Make a guess:")
    if choice.isdigit():
        choice=int(choice)
    else:
        print("Please type a number next time.")
        continue

    if choice==guess:
        print("You got it.")
        break
    else:
        if choice>guess:
            print("You were above the number")
        else:
            print("You were below the number")

print("You got it in", chance, "guesses")