while(True):
    S, E = map(int,input().split())
    if 2 <= S <= 9 and 2 <= E <= 9:
        break
    print("INPUT ERROR!")

if S < E:
    for i in range(1,10):
        for j in range(S, E+1): # 단
            print("%d * %d = %2d" % (j, i, j*i), end="   ")
        print()
else:
    for i in range(1,10):
        for j in range(S, E-1, -1): # 단
            print("%d * %d = %2d" % (j, i, j*i), end="   ")
        print()


