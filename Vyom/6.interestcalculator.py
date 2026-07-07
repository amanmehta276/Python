# Interest calculator

a=input("What kind of interest you want to calculage (Simple[S]/Compound[C]) : ")
P=int(input("Tell me Your principal ammount : "))
R=int(input("Tell me Your Interest Rate (%) : "))
T=int(input("Tell me the total time of interest : "))

if a=="S":
    b=(P*R*T)/100
    print(f"Your total simple interest is : {b}")
elif a=="C":
    n=int(input("Interest add in how many times a year : "))
    b=P*(1+(R/100)/n)**(n*T)
    print(f"You total compound interest is : {b}")