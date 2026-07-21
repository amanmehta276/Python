class Person:
    def __init__(self,name,car):
        self.__name=name
        self.__car=car        

        # __private

    def getName(self):    #getter
        return self.__name
    def setName(self,name):    #setter
        self.__name=name

    def getCar(self):
        return self.__car
    def setCar(self,car):
        self.__car=car

p=Person("Aman","Rollsroyce")

print(p.getName(),p.getCar())
p.setName("Mehta")
p.setCar("BMW")
print(p.getName(),p.getCar())