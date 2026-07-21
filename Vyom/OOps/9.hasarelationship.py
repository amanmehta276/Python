# Aggression=one object uses another object,but can exist without them too

# Person HAS_A car
# class Car:
#     def __init__(self,brand):
#         self.brand=brand

# class Person:
#     def __init__(self,name,car):
#         self.name=name
#         self.car=car

# c=Car("Rollsroyce")
# P=Person("Aman",c)

# print(P.name)
# print(P.car.brand)


# Composition=Without parent parent object child object cant exist
# House HAS_A room
# class Room:
#     def __init__(self):
#         print("Room created")
    
# class House:
#     def __init__(self):
#         self.room=Room()
#         print("House created")

# h=House()



# Nested Classes
class Outer:

    class Inner:

        def show(self):
            print("Inside Inner")

obj = Outer.Inner()

obj.show()