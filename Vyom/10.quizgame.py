# Python quiz game

questions = (
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "Who developed Python?",
    "What does CPU stand for?",
    "Which keyword is used to define a function in Python?"
)

options = (
    ("A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bjarne Stroustrup"),
    ("A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Utility"),
    ("A. func", "B. define", "C. def", "D. function")
)

answers = ("B", "B", "C", "B", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A , B , C , D) :").upper()
    if guess==answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num+=1

print("-----------------------------")
print("------------RESULTS----------")
print("-----------------------------")

print("Answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses: ",end="")
for guess in guesses:
    print(answer,end=" ")
print()

score=int(score/len(questions)*100)
print(f"Your score is : {score}%")