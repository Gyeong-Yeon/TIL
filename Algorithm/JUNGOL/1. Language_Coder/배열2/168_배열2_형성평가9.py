n = int(input())

arr = [[0]*n for _ in range(n)]
arr[0][0] = 1

for i in range(1, n):
    for j in range(n):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(n-1,-1,-1):
    for j in range(n):
        if arr[i][j] != 0:
            print(arr[i][j], end=" ")
    print()