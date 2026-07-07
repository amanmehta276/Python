# weight converter

weight=float(input("Enter your weight : "))
unit=input("Killogram or Pounds ? (Kg/F) : ")

if unit=="Kg":
    a=weight*2.20462
    print(f"Converting it into Pounds : {a}F")
elif unit=="F":
    a=weight/2.20462
    print(f"Converting it into Killograms : {a}Kg")