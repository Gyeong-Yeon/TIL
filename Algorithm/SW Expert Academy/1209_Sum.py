for _ in range(1,11):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    total = []

    rows = []
    for i in range(100): # 행의 합
        row = 0
        for j in range(100):
            row += arr[i][j]
        rows.append(row)
    total.append(max(rows))

    cols = []
    for i in range(100): # 열의 합
        col = 0
        for j in range(100):
            col += arr[j][i]
        cols.append(col)
    total.append(max(cols))

    dig1 = 0
    dig2 = 0
    for i in range(100): # 대각선의 합
       for j in range(100):
            if i == j:
                dig1 += arr[i][j]
            elif i+j == 99:
                dig2 += arr[i][j]
    total.append(dig1)
    total.append(dig2)

    result = max(total)

    print("#{} {}".format(tc, result))


