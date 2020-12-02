import sys
sys.stdin = open('input_Ladder1.txt')

def ladder():
    dr = [0, 0, 1]  # 좌, 우, 하
    dc = [-1, 1, 0]  # 좌, 우, 하

    for s in range(100):  # 출발점 : arr[0][s]
        i = 0
        j = s
        for d in range(3):  # d: 0, 1, 2
            while True:
                if d == 2:
                    # d 2랑 0 둘다 가능 할 때
                    if (0 <= i+dr[2] < 100 and 0 <= j+dc[2] < 100 and arr[i+dr[2]][j+dc[2]] == 1) and (
                            0 <= i+dr[0] < 100 and 0 <= j+dc[0] < 100 and arr[i+dr[0]][j+dc[0]] == 1):
                        i += dr[0]
                        j += dc[0]
                        if arr[i][j] == 2:
                            return s
                    # d 2랑 1 둘다 가능 할 때
                    elif (0 <= i+dr[2] < 100 and 0 <= j+dc[2] < 100 and arr[i+dr[2]][j+dc[2]] == 1) and (
                            0 <= i+dr[1] < 100 and 0 <= j+dc[1] < 100 and arr[i+dr[1]][j+dc[1]] == 1):
                        i += dr[1]
                        j += dc[1]
                        if arr[i][j] == 2:
                            return s
                    else:
                        break
                else:
                    if 0 <= i + dr[d] < 100 and 0 <= j + dc[d] < 100 and arr[i + dr[d]][j + dc[d]] == 1:
                        i += dr[d]
                        j += dc[d]
                        if arr[i][j] == 2:
                            return s
                    else:
                        break


for tc in range(1, 11):
    arr = [list(map(int,input().split())) for _ in range(100)]

    result = ladder()

    print("#{} {}".format(tc, result))





