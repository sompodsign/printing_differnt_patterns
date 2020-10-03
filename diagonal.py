def pattern(n):
    k = 2 * n - 2
    for i in range(n):

        for j in range(k):
            print(end=" ")
        
        for j in range(i+1):
            print("* ", end="")

        print()
        k = k - 1

    for i in range(n, -1, -1):

        for j in range(k, 0, -1):
          print(end=" ")

        for j in range(i+1):
            print("* ", end="")

        print()
        k=k+1







pattern(5)