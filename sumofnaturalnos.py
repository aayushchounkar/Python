#Write a Python Program to print first n Natural numbers and their sum.
n=int(input('Enter the range: '))
sum=0
for i in range(1,n+1):
    print(i,end="")
    sum+=i
print()
print('The sum of',n,'natural numbers is',sum)