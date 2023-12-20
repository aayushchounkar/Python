#Write a python function to find square and cube of a number
def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Example usage:
my_number = int(input("Enter a number="))
square_result, cube_result = calculate_square_and_cube(my_number)
print(f"The square of {my_number} is: {square_result}")
print(f"The cube of {my_number} is: {cube_result}")
