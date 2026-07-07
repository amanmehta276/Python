import math

f=int(input("Enter the number of turns: "))

a,b=0,1

for i in range(f):
    # if (f<2):
    #     print(f)
    #     # if f==f:
    #     #     break 
    # else:
    #     print(f+(f-1))
    #     # if f==f+(f-1):
    #     #     break.
    print(a,end=" ")
    a,b=b,a+b