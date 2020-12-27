def omok(color):

    for i in range(19): # 가로
        for j in range(15):
            if arr[i][j] == color:
                cnt = 1
                for d in range(1,6):
                    if j+d < 19 and arr[i][j+d] == color:
                        cnt += 1
                if cnt == 5:
                    if j-1 >= 0 and arr[i][j-1] == color:
                        continue
                    else:
                        return color, i, j


    for i in range(15): # 세로
        for j in range(19):
            if arr[i][j] == color:
                cnt = 1
                for d in range(1,6):
                    if i+d < 19 and arr[i+d][j] == color:
                        cnt += 1
                if cnt == 5:
                    if i-1 >= 0 and arr[i-1][j] == color:
                        continue
                    else:
                        return color, i, j


    for i in range(15): # 대각선 하
        for j in range(15):
            if arr[i][j] == color:
                cnt = 1
                for d in range(1,6):
                    if i+d < 19 and j+d < 19 and arr[i+d][j+d] == color:
                        cnt += 1
                if cnt == 5:
                    if i-1 >= 0 and j-1 >= 0 and arr[i-1][j-1] == color:
                        continue
                    else:
                        return color, i, j

    for i in range(4,19): # 대각선 상
        for j in range(4,19):
            if arr[i][j] == color:
                cnt = 1
                for d in range(1,6):
                    if i-d >= 0 and j-d >= 0 and arr[i-d][j-d] == color:
                        cnt += 1
                if cnt == 5:
                    if j - 1 >= 0 and arr[i][j - 1] == color:
                        continue
                    else:
                        if i+1 >= 0 and j+1 >= 0 and arr[i+1][i+1] == color:
                            continue
                        else:
                            return color, i, j

    return '0'


arr = [list(map(int,input().split())) for _ in range(19)]

black = list(omok(1))
white = list(omok(2))

if len(black) > 1:
    print(black[0])
    print("{} {}".format(black[1]+1, black[2]+1))
elif len(white) > 1:
    print(white[0])
    print("{} {}".format(white[1]+1, white[2]+1))
else:
    print("0")


