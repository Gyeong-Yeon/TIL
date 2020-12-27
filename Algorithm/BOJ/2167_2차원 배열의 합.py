N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
K = int(input())

for t in range(N): # 가로누적
    for b in range(1,M):
        arr[t][b] += arr[t][b-1]
for t in range(1,N): # 세로누적
    for b in range(M):
        arr[t][b] += arr[t-1][b]

for _ in range(K):
    i, j, x, y = map(int,input().split())
    if i == 1 and j == 1:
        result = arr[x-1][y-1]
    elif i == 1:
        result = arr[x-1][y-1] - arr[x-1][j-2]
    elif j == 1:
        result = arr[x-1][y-1] - arr[i-2][y-1]
    else:
        result = arr[x-1][y-1] - arr[x-1][j-2] - arr[i-2][y-1] + arr[i-2][j-2]

    print(result)



