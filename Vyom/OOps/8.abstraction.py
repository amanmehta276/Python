
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print("Sleeping")

# animal=Animal()
# animal.eat()

d=Dog()
d.eat()