def is_perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

# Example usage:
my_number = int(input("enter a number"))
result = is_perfect_number(my_number)

if result:
    print(f"{my_number} is a perfect number.")
else:
    print(f"{my_number} is not a perfect number.")
