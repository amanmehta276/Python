row=int(input("Enter number of rows : "))
column=int(input("Enter number of columns : "))
symbol=input("Enter the symbol : ")

for i in range(row):
    for j in range(column):
        print(symbol,end=" ")
    print()