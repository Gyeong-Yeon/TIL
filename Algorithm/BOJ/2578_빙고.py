def game():
    cnt = 0
    for i in range(5):
        for j in range(5):
            for t in range(5):
                for b in range(5):
                    if call[i][j] == bingo[t][b]:
                        bingo[t][b] = 0
                        cnt += 1
            if count() >= 3:
                return cnt

def count():
    bingo_cnt = 0

    for i in range(5): # 가로 빙고
        zero_cnt = 0
        for j in range(5):
            if bingo[i][j] == 0:
                zero_cnt += 1
        if zero_cnt == 5:
            bingo_cnt += 1

    for i in range(5): # 세로 빙고
        zero_cnt = 0
        for j in range(5):
            if bingo[j][i] == 0:
                zero_cnt += 1
        if zero_cnt == 5:
            bingo_cnt += 1

    zero_cnt = 0
    for i in range(5): # 대각선(/) 빙고
        if bingo[i][4-i] == 0:
            zero_cnt += 1
    if zero_cnt == 5:
        bingo_cnt += 1

    zero_cnt = 0
    for i in range(5):  # 대각선(\) 빙고
        if bingo[i][i] == 0:
            zero_cnt += 1
    if zero_cnt == 5:
        bingo_cnt += 1

    return bingo_cnt


bingo = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]

result = game()

print(result)