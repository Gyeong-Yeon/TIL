T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            arr[i][j] = 1

    for i in range(N):
        for j in range(i+1):
            if i-1 >= 0 and j-1 >= 0:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()

