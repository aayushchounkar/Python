#Write a python function to multiply all numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

my_numbers = [1, 2, 3, 4, 5]
result = multiply_list(my_numbers)
print(f"The product of the numbers is: {result}")
