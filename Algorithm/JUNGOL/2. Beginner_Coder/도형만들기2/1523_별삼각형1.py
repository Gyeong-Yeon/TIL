n, m = map(int,input().split()) # n: 높이, m: 종류

if 0 < n <= 100 and 1 <= m <= 3:
    if m == 1:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print('*', end="")
            print()
    elif m == 2:
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print('*', end="")
            print()
    elif m == 3:
        for i in range(1,n+1):
            empty = ' ' * (n-i)
            print(empty, end="")
            for j in range(1,2*i):
                print('*', end="")
            print()
else:
    print("INPUT ERROR!")

