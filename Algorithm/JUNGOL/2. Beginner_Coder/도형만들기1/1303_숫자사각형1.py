n, m = map(int,input().split())

s = 1
for _ in range(n):
    for _ in range(m):
        print(s, end=" ")
        s += 1
    print()

