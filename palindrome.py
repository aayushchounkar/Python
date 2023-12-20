def is_palindrome(input_string):
   
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]


my_string = str(input("Enter a string="))
result = is_palindrome(my_string)

if result:
    print(f'"{my_string}" is a palindrome.')
else:
    print(f'"{my_string}" is not a palindrome.')
