# Temperature converter


Temperature=float(input("Enter the Temperature : "))
unit=input("Celcius or Fahrenheits ? (C/F) : ")

if unit=="C":
    a=(Temperature*1.8)+32
    print(f"Converting it into Fahrenheit : {a}F")
elif unit=="F":
    a=(Temperature-32)/1.8
    print(f"Converting it into Celcius : {a}C")