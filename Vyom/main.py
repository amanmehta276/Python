# while executes soem code while some condition remains true 
# jab tak hiexecutes krega jab tak condtition true ho

# name=input("Your name: ")
# while name=="":
#     print("Enter it: ")
#     name=input("Name: ")

# print(f"Helloe {name}")

# for loop execute a programm for a fixed amount of time
# Aman="AMAN"
# for x in Aman:
#     print(x)


# nested loop =loop inside a loop

# for i in range(3):
#     for j in range(1,11):
#         print(j,end=" ")
#     print()


# list[],set{},tuple()
# list=[] ordered , mutable , duplicate
# set={} unordered,mutable,no duplicate
# tuple=() ordered,immutable,duplicate
# together they are called collection 

# fruit=["apple","orange","banana","coconut"]

# print(fruit[0])

# for i in fruit:
#     print(i)

# print(dir(fruit)) give all things we can do here 
# print(help(fruit)) give all methods

# num=[1,2,3,4,5,3,4,6]
# num.sort()
# print(num)

# 2d list

# students = ["Aman", "Rahul", "Priya", "Neha"]

# cities = ["Delhi", "Mumbai", "Bhopal", "Jaipur"]

# marks = [85, 92, 78, 88, 95]

# total=[students,cities,marks]
# # print(total)

# for i in total:
#     for j in i:
#         print(j,end=" ")
#     print()

# numpad
# num_pad=((1,2,3),
#          (4,5,6),
#          (7,8,9),
#          ("*",0,"#"))

# for i in num_pad:
#     for j in i:
#         print(j,end=" ")
#     print()

# dictionary=a collection of key,value pairs,ordered and changegable and no dupllicate
# student = {
#     "name": "Aman",
#     "age": 19,
#     "course": "B.Tech", 
#     "is_student": True
# }
# print(student)



# import random

# # print(help(random))
 
# low=0
# high=100
# options=("rock","paper","scissors")
# # number=random.randint(low,high)
# option=random.choice(options)
# print(option)

# fuction =reusable codes which needs to be called


# def add(**kwargs):
#     total=0
#     for key in kwargs.keys():
#         print(key)

# add(street="123",city="ok")
# # print(add())
# # print(type(add))


# num=[1,2,3,4,5]

# for n in num:
#     print(n)


# doubles=[]

# for x in range(1,11):
#     doubles.append(x*2)

# print(doubles)

# doubles=[ x*2 for x in range(1,11)]
# print(doubles)

# num=[1,-2,3,-4,-5]
# pnum=[n for n in num if n>=0]
# print(pnum)

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It's Sunday"
#         case 2:
#             return "It's Monday"
#         case 3:
#             return "It's Tuesday"
#         case 4:
#             return "It's Wednesday"
#         case 5:
#             return "It's Thursday"
#         case 6:
#             return "It's Friday"
#         case 7:
#             return "It's Saturday"
#         case _:
#             return "Invalid day number"

# # _ the ast one is called wildcard statement

# day=int(input("enter the numver of the day: "))
# # print(day_of_week(1))  # It's Sunday
# # print(day_of_week(5))  # It's Thursday
# # print(day_of_week(8))  # Invalid day number

# print(day_of_week(day))


# print(help("modules"))

# import math as m

# print(m.pi)
# import module
# from module import square

# print(square(3))

# a=9
# def fun():
#     x=1
#     print(a)
#     def fun8():
#         print(x)
#     fun8()

# def fun6():
#     y=1
#     print(y)

# fun()
# fun6()



# ASK to user

# def personal():
#     name=input("Enter your name: ")
#     age=int(input("enter your age: "))
#     college=input("Enter your colleege: ")
#     plang=input("Enter your fvrt programming language: ")
#     dream_cmpny=input("Enter Your dream Compnay: ")

#     print(f"My name is {name}")
#     print(f"I am {age} years old")
#     print(f"My college name is {college}")
#     print(f"My favroite programming language is {plang}")
#     print(f"My dream compnay is {dream_cmpny}")

# personal()

# import random

# number=random.randint(1,100)

# a=input("Enter you name: ")
# print(f"{number} is lucky number for you ")

# import random 

# print(random.randint(1000,9999))

# multple inheritance
# class Father:
#     def father(self):
#         print("Father's property")

# class Mother:
#     def mother(self):
#         print("Mother's property")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.father()
# c.mother()

# medieval inheritance
# class Grandfather:
#     def grand(self):
#         print("Grandfather")

# class Father(Grandfather):
#     def father(self):
#         print("Father")

# class Son(Father):
#     def son(self):
#         print("Son")

# s = Son()
# s.grand()
# s.father()
# s.son()


# polymorphism = same function name but different functionality
# many form

# from abc import ABC,abstractmethod
# class Shape:

#     @abstractmethod
#     def area(self):
#        pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius

# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**2

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
    
#     def are(self):
#         return 0.5*self.base*self.height

# # square =Square()

# shapes=[Circle(4),Square(5),Triangle(6,7)]

# for shape in shapes:
#     print(shape.area)