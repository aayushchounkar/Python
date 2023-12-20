# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#           print("Name=",self.name,"age=",self.age)
# obj=Student("Chounkyyyyy",18)
# obj.display()
# obj1=Student("ashhhhhh",19)
# obj1.display()



#display count of objects paramatarise constructor
# class Student:
#     count=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Student.count+=1
#     def display(self):
#           print("Name=",self.name,"age=",self.age)
#           print("count=",Student.count)
# obj=Student("Chounkyyyyy",18)
# obj.display()
# obj1=Student("ashhhhhh",19)
# obj1.display()

# class ITM:
#     def __init__(self,name,age,department):
#         self.name=name
#         self.age=age
#         self.department=department
#     def get(self):
#         name = input("enter the name :")
#         age = input("enter the age :")
#         department = input("enter your department")
#         ITM.admited_stu=+1
#     def display(self):
#         print("Name=",self.name,"Age=",self.age,"Department=",self.department)
#         print("Student in",ITM.admited_stu)
# obj=ITM()
# obj.get()
# obj.display()



# class Student:
#     def __init__(self,name,age,dept): #This is used 
#         self.name = name
#         self.age = age 
#         self.department = dept 
#         Student.count =+1
#     def display(self):
#         print("name : ",self.name,"Age :",self.age,"department :",self.department)
#         print(Student.count)

# name = input("enter the name :")
# age = int(input("enter the age :"))
# dept = input("enter your department-")

# obj1 = Student(name,age,dept)
# obj1.display()

#CLASS DEMONSTRATION
# class TestClas():
#     def __init__(self):
#         self.name=None
#         self.age=None
#         self.dept=None


# objs=list()
# for i in range(10):
#     objs.append(TestClas())

# print(objs)

# objs[0].name="AAYUSH"
# objs[0].age=19

# print(objs[0].name)
# print(objs[0].age)

class Student:
    
    count = 0
    
    def __init__(self):
        self.name = input("Enter Student Name: ")
        self.age = int(input("Enter Student Age: "))
        self.department = input("Enter Student Department (PGDM(p)/B.Tech(b)): ").capitalize()
        
        Student.count += 1

    def display(self):
        print("Name:", self.name, "Age:", self.age, "Department:", self.department)

print("""------ STUDENT ADMIT ------""")

pgdm_students = []
btech_students = []

num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    new_student = Student()
    new_student.display()
    
    if new_student.department == 'P':
        pgdm_students.append(new_student)
    
    elif new_student.department == 'B':
        btech_students.append(new_student)

print("*******")

print("\nPGDM Department Students:")
for student in pgdm_students:
    student.display()

print("\nB.Tech Department Students:")
for student in btech_students:
    student.display()

print("\nTotal number of students:", Student.count)