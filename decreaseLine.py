def pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i):
            print("* ", end="")
        print("\r")
        
pattern(4) 