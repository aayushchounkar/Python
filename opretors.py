print ("1.arithmetic")
print ("2.Identity")
print ("3.Bitwise")
print ("4.logical")
print ("5.membership")
print ("6.relational")
print ("7.ternary")
print ("8.assignment")
#arithmetic
operator = input("Enter operator (1,2,3,4,5,6,7,8): ")
if operator == '1':
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid operator")
    
        print(f"Result: {result}")
#identity 
if operator == '2':
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
# Identity Operators
    print("Identity Operators Showcase:")
    print(f"a = {a}")
# is Operator
    print(f"a is b: {a is b}")
# is not Operator
    print(f"a is not b: {a is not b}")
#bitwise
if operator == '3':
    a = 5  # Binary: 0101
    b = 3  # Binary: 0011
    # Bitwise Operators
    print("Bitwise Operators Showcase:")
    print(f"a = {a} (Binary: {bin(a)})")
    print(f"b = {b} (Binary: {bin(b)})")
    # Bitwise AND
    result_and = a & b
    print(f"a & b: {result_and} (Binary: {bin(result_and)})")
    # Bitwise OR
    result_or = a | b
    print(f"a | b: {result_or} (Binary: {bin(result_or)})")
    # Bitwise XOR
    result_xor = a ^ b
    print(f"a ^ b: {result_xor} (Binary: {bin(result_xor)})")
    # Bitwise NOT
    result_not_a = ~a
    print(f"~a: {result_not_a} (Binary: {bin(result_not_a)})")
    # Bitwise Left Shift
    result_left_shift = a << 1
    print(f"a << 1: {result_left_shift} (Binary: {bin(result_left_shift)})")
    # Bitwise Right Shift
    result_right_shift = a >> 1
    print(f"a >> 1: {result_right_shift} (Binary: {bin(result_right_shift)})")
#logical
if operator == '4':
    x = True
    y = False
    # Logical Operators
    print(f"x = {x}, y = {y}")
    # Logical AND
    result_and = x and y
    print(f"x and y: {result_and}")
    # Logical OR
    result_or = x or y
    print(f"x or y: {result_or}")
    # Logical NOT
    result_not_x = not x
    result_not_y = not y
    print(f"not x: {result_not_x}")
    print(f"not y: {result_not_y}")
#
if operator == '5':
    list_example = [1, 2, 3, 4, 5]
    element_1 = 3
    element_2 = 6

    # Membership Operators
    print("Membership Operators Showcase:")
    print(f"list_example = {list_example}")

    # in Operator
    print(f"{element_1} in list_example: {element_1 in list_example}")

    # not in Operator
    print(f"{element_1} not in list_example: {element_1 not in list_example}")
if operator == '6':

    a = (input("Enter the value for variable 'a': "))
    b = (input("Enter the value for variable 'b': "))
    # Relational Operators
    print("Relational Operators:")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} >= {b}: {a >= b}")
if operator == '7':
    a = 5
    b = 10
    # Ternary-like Operator
    result = "a is greater than b" if a > b else "a is less than or equal to b"
    # Output
    print("Ternary-like Operator Showcase:")
    print(result)
if operator == '8':
    a = 5
    b = 10

    # Assignment Operators
    print("Assignment Operators Showcase:")
    print(f"Initial values: a = {a}, b = {b}")
    # Addition assignment
    a += 3
    print(f"After a += 3: a = {a}")
    # Subtraction assignment
    b -= 5
    print(f"After b -= 5: b = {b}")
    # Multiplication assignment
    a *= 2
    print(f"After a *= 2: a = {a}")
    # Division assignment
    b /= 2
    print(f"After b /= 2: b = {b}")
    # Modulus assignment
    a %= 3
    print(f"After a %= 3: a = {a}")
    # Exponentiation assignment
    b **= 2
    print(f"After b **= 2: b = {b}")
    # Floor Division assignment
    a //= 2
    print(f"After a //= 2: a = {a}")

elif operator == '0':
    print('invalid operator') 

else:
    print('invalid operator')