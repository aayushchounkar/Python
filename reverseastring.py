#Write a python function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

original_string = str(input("Enter a string to reverse="))
reversed_string = reverse_string(original_string)
print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_string}")
