print("Welcome to the game!")

playing=input("Do you wanna play ? (yes/no) ")
print(playing)

if playing.lower()!="yes":
    quit() #quit the program imedietly

print("Okay! Let's play :) ")
score=0

answer=input("What does CPU stands for? ")

if answer=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Hell naah bro please go and read some books")



answer1=input("What is India's Capital ? ")

if answer1=="New Delhi ":
    print("Correct!")
    score+=1
else:
    print("Hell naah bro please go and read some books")

print("You got" + str(score) + "questions correct")
print("You got" + str((score/2)*100) + " % .")