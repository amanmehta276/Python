# lists=["AMAN","ASH","RED","BLUE","GREEN","YELLOW"]

# # obj1=enumerate(list)

# print(list(enumerate(lists,1)))
x=int(input("Enter x: "))
y=int(input("Enter y: "))
sum=lambda x,y:x+y
sub=lambda x,y:x-y
mul=lambda x,y:x*y
div=lambda x,y:x/y
print(sum(x,y))
print(sub(x,y))
print(mul(x,y))
print(div(x,y))