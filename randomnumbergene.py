# import random
# random_number = random.randint(1,47)
# print("Random Number:", random_number)


import random
start_range = 1
end_range = 47

random_numbers = random.sample(range(start_range, end_range + 1), k=10)
print("Random Numbers without repetition:", random_numbers)

