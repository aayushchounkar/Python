#Write a Python program to print table of a given number.
num=int(input('Enter number you want to print the table of: '))
for i in range(1,11,2):
    print(num,'X',i,'=',i*num)
