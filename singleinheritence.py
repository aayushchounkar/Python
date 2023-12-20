# Single Inheritence
# class addition:
#     def add(self, a, b):
#         return a + b

# class user_input(addition):
#     def get_user_input(self):
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         return num1, num2


# user_input_adder = user_input()
# numbers = user_input_adder.get_user_input()
# result = user_input_adder.add(*numbers)
# print(f"The sum of {numbers[0]} and {numbers[1]} is: {result}")


#Area of square
# class Shape:
#     def calculate(self, a ,b ):
#         return a*b
    
# class user_input(Shape):
#     def get_user_input(self):
#         num1=int(input("Enter a number for side one"))
#         num2=int(input("Enter a number for other side"))
#         return num1,num2

# user_input_calculate=user_input()
# nums=user_input_calculate.get_user_input()
# result=user_input_calculate.calculate(*nums)
# print(f"The area of square is {nums[0]} and {nums[1]} is: {result}")



#option of rectangle and square 
# class AreaCalculator:
#     def __init__(self):
#         self.length = 0
#         self.width = 0

#     def get_user_input(self):
#         self.length = int(input("Enter the length: "))
#         self.width = int(input("Enter the width : "))

#     def calculate_square_area(self):
#         return self.length * self.length

#     def calculate_rectangle_area(self):
#         return self.length * self.width

#     def display_results(self, shape):
#         if shape == "square":
#             area = self.calculate_square_area()
#         elif shape == "rectangle":
#             area = self.calculate_rectangle_area()
#         else:
#             print("Invalid shape specified")

#         print(f"Area of {shape} is: {area}")

# calculator = AreaCalculator()

# shape_choice = input("Enter the shape (square/rectangle): ").lower()
# calculator.get_user_input()

# if shape_choice == "square":
#     calculator.display_results("square")
# elif shape_choice == "rectangle":
#     calculator.display_results("rectangle")
# else:
#     print("Invalid shape specified. Please enter 'square' or 'rectangle'.")

# area of square and rectangle in one function 
class Parent:
    def area(self, x, y = None):
        if y is None:
            return x * x
        else:
            return x * y

class Child(Parent):
    def take_values(self):
        self.option = int(input("Enter 1 for square or 2 for rectangle: "))
        if self.option == 1:
            self.x = int(input("Enter the length of side for area of square: "))
        elif self.option == 2:
            self.x = int(input("Enter the length for area of rectangle: "))
            self.y = int(input("Enter the breadth for area of rectangle: "))
        else:
            print("Invalid Option")

obj = Child()
obj.take_values()

if obj.option == 1:
    print("Area of the square is: ", obj.area(obj.x))
elif obj.option == 2:
    print("Area of the rectangle is: ", obj.area(obj.x, obj.y))