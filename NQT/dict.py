# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
a=min(prices)

for i in range(len(prices)):
    if prices[i]==a:
        b=i
        c=prices[i:]

d=max(c)
# print(d)

for i in range(len(prices)):
    comp=d-a

print(comp)