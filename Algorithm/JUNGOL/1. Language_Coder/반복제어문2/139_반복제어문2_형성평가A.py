S, E = map(int,input().split())

if S > E:
    for i in range(1, 10):
        for j in range(S,E-1,-1):
            print("%d * %d = %2d" % (j, i, j*i), end="   ")
        print()
else:
    for i in range(1, 10):
        for j in range(S,E+1):
            print("%d * %d = %2d" % (j, i, j*i), end="   ")
        print()

