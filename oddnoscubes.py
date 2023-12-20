  #WAP that creates a dictionary of cubes of odd numbers in th range 1 to 10
cubes_dict = {}
for num in range(1, 11, 2):  
    cubes_dict[num] = num**3
print(cubes_dict)
