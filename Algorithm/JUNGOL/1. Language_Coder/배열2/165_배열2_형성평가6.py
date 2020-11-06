arr = [[1, 0, 1, 0, 1]] + [[0]*5 for _ in range(4)]

for i in range(1,5):
    for j in range(5):
        if j-1 < 0:
            arr[i][j] = arr[i-1][j+1]
        elif j+1 >= 5:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

for i in range(5):
    for j in range(5):
        print(arr[i][j], end=" ")
    print()