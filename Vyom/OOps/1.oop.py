class Car:
    def __init__(self,name,country=0,price=0):
        self.name=name
        self.country=country
        self.price=price

    def show(self):
        return f"{self.name}"

a=Car("Aman")
print(a.show())