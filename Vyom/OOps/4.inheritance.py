# class Animal:
#     def __init__(self,name):
#         self.name=name
#         self.is_alive=True

#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Dog(Animal):
#     # def __init__(self,name):
#         pass

# class Cat(Animal):
#     pass

# dog=Dog("Lio")
# cat=Cat("Tom")

# print(dog.name)
# print(dog.is_alive)
# cat.eat()
# cat.sleep()


# Multiple and Multilevel inheritance

class Animal:
    def eat(self):
        print("This animal is eating ")
    
    def eat(self):
        print("This animal is sleeping")

class Prey(Animal):
    def flee(self):
        print("It is fleeing")

class Predator(Animal):
    def hunt(self):
        print("It is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

e=Rabbit()
h=Hawk()
# f=Fish()
e.flee()
h.hunt()
# f.flee()
# f.hunt()
e.eat()