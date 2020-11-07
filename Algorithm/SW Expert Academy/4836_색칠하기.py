T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    for _ in range(N): # 색칠하기
        rs, cs, re, ce, color = map(int,input().split())
        # rs: 행 시작, re: 행 끝
        # cs: 열 시작, ce: 열 끝
        for i in range(rs,re+1):
            for j in range(cs,ce+1):
                arr[i][j] += color

    purple = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                purple += 1

    print("#{} {}".format(tc, purple))


