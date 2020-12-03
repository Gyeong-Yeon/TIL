def omok(color):
    for i in range(19): # 가로
        for j in range(15):
            if arr[i][j] == color:
                cnt = color
                for d in range(1,6):
                    if j+d < 19 and arr[i][j+d] == color:
                        cnt += 1
                if cnt == 5:
                    x = i
                    y = i
                    break

    for i in range(15): # 세로
        for j in range(19):
            if arr[j][i] == color:
                cnt = color
                for d in range(1,6):
                    if i+d < 19 and arr[j][i+d] == color:
                        cnt += 1
                if cnt == 5:
                    x = i
                    y = i
                    break

    for i in range(15): # 대각선 상
        for j in range(15):
            if arr[i][j] == color:
                cnt = 1
                for d in range(1,6):
                    if i+d < 19 and j+d < 19 and arr[i+d][j+d] == color:
                        cnt += 1
                if cnt == 5:
                    x = i
                    y = i
                    break

    for i in range(4,19):
        for j in range(4,19):
            if arr[i][j] == color:
                cnt = 1
                for d in range(1,6):
                    if i-d >= 0 and j-d >= 0 and arr[i-d][j-d] == color:
                        cnt += 1
                if cnt == 5:
                    x = i
                    y = i
                    break

    return x, y

arr = [list(map(int,input().split())) for _ in range(19)]

print(omok(1))
print(omok(2))