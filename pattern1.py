n = 7

s = 2 * n-2

for k in range(n, -1, -1):

    for m in range(s, 0, -1):

        print(end=" ")

    s = s + 1

    for m in range(0, k + 1):

        print("*", end=" ")

    print("")

