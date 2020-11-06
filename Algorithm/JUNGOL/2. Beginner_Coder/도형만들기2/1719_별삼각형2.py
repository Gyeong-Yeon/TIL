n, m = map(int,input().split())

if 0 < n <= 100 and n % 2 == 1 and 1 <= m <= 4:
    if m == 1:
        for i in range(1, n+1):
            mid = n//2 + 1
            if i <= mid:
                for j in range(1, i+1):
                    print('*', end="")
                print()
            else:
                for j in range(1, n-i+2):
                    print('*', end="")
                print()
    elif m == 2:
        for i in range(1, n + 1):
            mid = n // 2 + 1
            if i <= mid:
                empty = ' ' * (mid-i)
                print(empty, end="")
                for j in range(1, i+1):
                    print('*', end="")
                print()
            else:
                empty = ' ' * (i - mid)
                print(empty, end="")
                for j in range(1, n-i+2):
                    print('*', end="")
                print()
    elif m == 3:
        for i in range(1, n + 1):
            mid = n // 2 + 1
            if i <= mid:
                empty = ' ' * (i-1)
                print(empty, end="")
                for j in range(1, n+3-2*i):
                    print('*', end="")
                print()
            else:
                empty = ' ' * (n-i)
                print(empty, end="")
                for j in range(1, 2*i-n+1):
                    print('*', end="")
                print()
    elif m == 4:
        for i in range(1, n + 1):
            mid = n // 2 + 1
            if i <= mid:
                empty = ' ' * (i-1)
                print(empty, end="")
                for j in range(1, mid+2-i):
                    print('*', end="")
                print()
            else:
                empty = ' ' * (mid-1)
                print(empty, end="")
                for j in range(1, i+2-mid):
                    print('*', end="")
                print()
else:
    print("INPUT ERROR!")
