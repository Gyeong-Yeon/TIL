N = int(input())

arr = [[0]*100 for _ in range(100)]
for _ in range(N):
    R, C = map(int,input().split())
    for i in range(R, R+10):
        for j in range(C, C+10):
            arr[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)