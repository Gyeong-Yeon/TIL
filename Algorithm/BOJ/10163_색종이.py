N = int(input())

arr = [[0]*101 for _ in range(101)]
for c in range(1, N+1): # 색종이 별
    sr, sc, rr, rc = map(int,input().split())
    # sr: 시작 행, sc: 시작 열, rr: 행 범위, rc: 열 범위

    for i in range(sr, sr+rr):
        for j in range(sc, sc+rc):
            arr[i][j] = c

for c in range(1, N+1):
    cnt = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j] == c:
                cnt += 1
    print(cnt)


