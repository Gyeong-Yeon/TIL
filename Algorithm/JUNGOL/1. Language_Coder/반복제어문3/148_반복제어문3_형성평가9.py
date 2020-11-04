n = int(input())

l = 2*n - 1

for i in range(1,n):
    for j in range(i):
        print('#', end=" ")
    print()

for i in range(n,0,-1):
    empty = ' ' * (l-(2*i-1))
    print(empty, end="")
    for j in range(i):
        print('#', end=" ")
    print()