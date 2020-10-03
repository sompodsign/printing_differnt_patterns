def pattern(n):
    k = 2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        for j in range(i+1):
            print("* ", end="")
        print()
        k -= 1



pattern(5)