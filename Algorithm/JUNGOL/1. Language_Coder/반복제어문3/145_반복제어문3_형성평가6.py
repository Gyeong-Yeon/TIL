n = int(input())

l = 2*n - 1
for i in range(1,n+1):
    empty = ' ' * (l-2*i+1)
    print(empty, end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
