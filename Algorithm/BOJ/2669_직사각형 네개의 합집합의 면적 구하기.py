arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    sx, sy, ex, ey = map(int,input().split())
    for x in range(sx, ex):
        for y in range(sy,ey):
            arr[x][y] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)

