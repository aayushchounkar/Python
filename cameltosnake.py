camelcase = input("Enter a camel case string: ")

snakecase = ''
for char in camelcase:
    if char.isupper():
        snakecase += '_' + char.lower()
    else:
        snakecase += char

snakecase = snakecase.lstrip('_')

print("Snake case:", snakecase)

