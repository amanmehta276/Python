# class Car:
#     def __init__(self,model,year,color,for_sale):
#         self.model=model
#         self.year=year
#         self.color=color
#         self.for_sale=for_sale
    
#     def drive(self):
#         print(f"You drive the {self.model}")
    
#     def stop(self):
#         print(f"You stop the {self.model}")

# car1=Car("Mustang",2026,"red",False)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# inheritance
class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating ")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog=Dog("Scooby")
cat=Cat("Ku")

print(dog.eat())
print(cat.name)