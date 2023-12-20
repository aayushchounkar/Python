#Write a python function to calculate factorial of a number (non-negative integer)
def multiply_list(numbers):
    result = 1
    n= 1
    for i in range (numbers):
        result = result * n
        n = n+1
    return result

my_numbers = int(input("Enter a number"))
result = multiply_list(my_numbers)
print(f"The product of the numbers is: {result}")
