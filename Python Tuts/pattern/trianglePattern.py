def star_pattern(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ",end="")
        for j in range(0,((i*2)+1)):
            print("*",end="")
        print()

star_pattern(5)