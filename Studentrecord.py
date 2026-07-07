class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def __str__(self):
        return f"Name: {self.name},Roll:{self.roll},Marks:{self.marks}"

students=[]

def add_student():
    name=input("Enter name: ")
    roll=int(input("\nEnter the Roll no: "))
    marks=float(input("\nEnter marks: "))
    student=Student(name,roll,marks)
    students.append(student)
    print("student record added")

def display():
    if not students:
        print("Nothing has been found yet")
    else:
        print("\n Students records:")
        for s in students:
            print(s,end=" ")

def search_by_roll():
    roll=int(input("Enter the roll no for search: "))
    for s in students:
        if s.roll==roll:
            print(f"Found: {s}")
        else:
            print("studnets data not found")

def sort_by_marks():
    n=len(students)
    for i in range(n):
        for j in range(0,n-i-1):
            if students[j].marks>students[j+1].marks:
                students[j],students[j+1]=students[j+1],students[j]
    for s in students:
        print(f"Records sorted: {s}")

def delete():
    roll=int(input("Enter the roll no to delete: "))
    for s in students:
        if s.roll==roll:
            students.remove(s)
            print("student data deleted")
        else:
            print("No students found")

def menu():
    while True:
        print("\n--- Student record system ---")
        print("1.Add student")
        print("2.Dsiplay All")
        print("3.Search by Roll")
        print("4.Sort by marks")
        print("5.Delete student")
        print("6.Exit")
        choice=input("Choose and option: ")
        if choice=='1':
            add_student()
        elif choice=='2':
            display()
        elif choice=='3':
            search_by_roll()
        elif choice=="4":
            sort_by_marks()
        elif choice=="5":
            delete()
        elif choice=="6":
            print(" Existing ")
            break
        else:
            print(" Invalid ")

menu()
# add_student()
# delete()
# display()
# search_by_roll()
# sort_by_marks()



'''
# DSA topics used 
class and object=class student
List=studennts=[]
Linear search=in search_by_roll()
and delete()
Bubble sort sort_by_marks()

Data structue:
Class
List
object
menusystem

Algorithms:
Linear search
Bubble sort
Traversal
swap logic
'''



