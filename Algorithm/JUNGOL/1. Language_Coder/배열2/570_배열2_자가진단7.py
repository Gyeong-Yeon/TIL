arr = [[1, 1, 1, 1, 1]] + [[0]*5 for _ in range(4)]

for i in range(1,5): # 채우기
    arr[i][0] = 1
    for j in range(1,5):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for i in range(5): # 출력
    for j in range(5):
        print(arr[i][j], end=" ")
    print()