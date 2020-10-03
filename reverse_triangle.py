def pattern(n):
    k = 2 * n -2
    for i in range(n, -1, -1):
        for j in range(k):
            print(end=" ")
        k += 1
        for j in range(i):
            print("* ", end="")
        print()



pattern(5)
