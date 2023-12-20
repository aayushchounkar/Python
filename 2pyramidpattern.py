n = int(input("enter a number"))
 # upward pyramid
for i in range(n-2):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()

# upward pyramid
for i in range(1,n-1):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()

#  upward pyramid
for i in range(1,n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()

for j in range (0,n):
    for i in range (3,n+1):   
        print(" ",end= "")
    for i in range (3,n+1):   
        print("*",end= "")
    print()

