class Math:
    def add(self,a,b=0,c=0):
        return a+b+c
    
m=Math()

print(m.add(10))
print(m.add(10,20))
print(m.add(10,20,30))