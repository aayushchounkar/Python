# my_tup=("ash",18,44)
# # a=(my_tup[0])
# # print(a)
# # b=print(my_tup[1])
# # c=print(my_tup[2])
# a,b,c=my_tup
# print(a)
# print(b)
# print(c)


# samdata=[(),(''),('a','b'),('a','b','c')]
# print(samdata)
# removetup=[t for t in samdata if bool (t)]
# print(removetup)


#WAP to unzipe a list of tupple into individual list
# l=[(1,2),(3,4),(8,9)]
tuples = [(6, 'hello'), (2, 'devil'), (3, 'orry')]
numbers = []
names = []
for item in tuples:
    number, name = item
    numbers.append(number)
    names.append(name)
print("Numbers:", numbers)
print("Names:", names)
