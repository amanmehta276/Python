h=float(input("Enter your Height(in meters): "))
w=int(input("Enter your Weight: "))
bmi=w/(h*h)
print("\nHeight=",h)
print("Weight=",w)
print("Your bmi is: ",bmi)
if (bmi==18.5)or(bmi==24.9):
    print("You are Healthy")
elif bmi<18.5:
    print("You are Underweight")
elif (bmi>=25)or(bmi<=29.9):
    print("You are Overweight")
else:
    print("You are Obese")