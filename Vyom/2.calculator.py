# Calculator

add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b

sign=input("Enter what u want to do (+ - * / all): ")
a=float(input("Enter a: "))
b=float(input("Enter b: "))

if sign=="+":
    print("Addition : ",add(a,b))
elif sign=="-":
    print("Subtraction : ",sub(a,b))
elif sign=="*":
    print("Multiplpication :",mul(a,b))
elif sign=="/":
    print("Division :",div(a,b))
elif sign=="all":
    print("Addition : ",add(a,b))
    print("Subtraction : ",sub(a,b))
    print("Multiplpication :",mul(a,b))
    print("Division :",div(a,b))