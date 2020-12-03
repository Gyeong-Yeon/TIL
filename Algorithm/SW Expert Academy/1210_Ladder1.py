import sys
sys.stdin = open('input_Ladder1.txt')

def ladder():
    dr = [0, 0,-1]  # 좌, 우, 상
    dc = [-1, 1,0]  # 좌, 우, 상

    for e in range(100):
        if arr[99][e] == 2:
            i = 99
            j = e
            while i > 0:
                for d in range(3): # d: 0, 1, 2
                    if 0 <= i+dr[d] < 100 and 0 <= j+dc[d] < 100 and arr[i+dr[d]][j+dc[d]] == 1:
                        arr[i][j] = 0
                        i += dr[d]
                        j += dc[d]
            return j

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    start = ladder()

    print("#{} {}".format(tc, start))






