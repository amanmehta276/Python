# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# d=Dog()
# c=Cat()
# d.sound()
# c.sound()

# a=[d,c]

# for i in a:
#     i.sound()

# Inheritance polymorphism

from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius**2
    
class Square(Shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        return self.side**2
    
shapes=[Circle(3),Square(3)]

for i in shapes:
    print(f"{i.area()} cm")