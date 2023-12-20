#WAP to creat list tupple dict of seven elements 
#WAP to creat tupple of different datatypes
#WAP to arrange list in decending order
#WAP to demonstrate control statement break/loop control statement break
#write a program to manage a library catlog use control statement to add ,searchfor,and maintain library inventory management 


# #program1
# l1=[1,2,3,4,5,6,7]
# print("list=",l1)
# tple=(7,5,4,2,3,4,5)
# print("tupple=",tple)
# d={1:"hello","tech":33,"saisir":(1,2,3,4)}
# print("dict=",d)

# #program2
# t2=(1,"hello",True,False,3.34)
# print(t2)
# print(type(t2))
# print(type(t2[0]))
# print(type(t2[1]))
# print(type(t2[2]))
# print(type(t2[3]))
# print(type(t2[4]))


#program3
# arr = [43,1,3,4,2]
# n = len(arr)

# for i in range(n-1):
#     for j in range(n-1):
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp

# sortedArr = list(arr[i] for i in range(n-1,-1, -1))
# print(sortedArr)


#program4
# for i in range(5):
#     for j in range(5):
#         print(i, j)
#         if j == 2:
#             print("Breaking inner loop at j =", j)
#             break

# i = 0
# while i <6:
#   print(i)
#   if (i == 4):
#     break
#   i += 1

print("**Welcome to the library**")
print("Which book do you want to read")
print("1.Harry Potter""\n""2.Physics""\n""3.Chemistry""\n""4.do you want to add any book?")
chemistry = 4
physics = 3
Harry_Potter = 2
choice =int(input("Enter your choice"))
if choice ==1:
    print("Here is the book")
    Harry_Potter=Harry_Potter-1
    print("Quantity remaing is",Harry_Potter)
elif choice ==2:
    print("Here is the book")
    physics=physics-1
    print("Quantity remaing is",physics)
elif choice ==3:
    print("Here is the book")
    chemistry=chemistry-1
    print("Quantity remaing is",chemistry)
elif choice ==4:
    print("Which book do you want to add?")
    print("1.Harry Potter""\n""2.Physics""\n""3.Chemistry")
    add = int(input("Enter your choice"))
    if add == 1:
     quantity = int(input("Enter the qty"))
     Harry_Potter=Harry_Potter+quantity
     print("Total qty no is",Harry_Potter)
    elif add == 2:
     quantity = int(input("Enter the qty"))
     physics=physics + quantity
     print("Total qty no is",physics)
    elif add == 3:
     quantity = int(input("Enter the qty"))
     chemistry= chemistry+quantity
     print("Total qty no is",chemistry)