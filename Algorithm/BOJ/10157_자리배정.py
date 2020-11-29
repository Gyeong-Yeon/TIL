def snail():
    arr = [[0] * C for _ in range(R)]

    dc = [0, 1, 0, -1] # 가로 방향
    dr = [1, 0, -1, 0] # 세로 방향

    i = -1
    j = 0
    cnt = 0
    while True:
        for d in range(4):
            while True:
                if 0 <= i+dr[d] < R and 0 <= j+dc[d] < C and arr[i+dr[d]][j+dc[d]] == 0:
                    cnt += 1
                    i += dr[d]
                    j += dc[d]
                    arr[i][j] = cnt
                    if cnt == K:
                        return i, j
                else:
                    break

C, R = map(int,input().split()) # C: 가로, R: 세로
K = int(input())

if K <= C*R:
    i, j = snail()
    print("{} {}".format(j+1, i+1))
else:
    print("0")