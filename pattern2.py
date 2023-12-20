# heart pattern
n = 6

# # upper part of heart
for i in range(n//2, n, 2):
    # print first spaces
    for j in range(1, n-i, 2):
        print(" ", end="")
    # print first alphabet
    for j in range(i):
        print(chr(65 + j), end="")
    # print second spaces
    for j in range(1, n-i+1, 1):
        print(" ", end="")
    # print second alphabet
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# lower part
for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i*2):
        print(chr(65 + j), end="")
    print()
    



