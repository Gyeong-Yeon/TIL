N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# index = 0:5, 1:3, 2:4

match = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

adds = [] # 합 리스트
for i in range(6): # arr[0][i]
    bottom = arr[0][i]
    top = arr[0][match[i]]

    initial_max = 0
    for j in range(6):
        if j != i and j != match[i]:
            if arr[0][j] > initial_max:
                initial_max = arr[0][j]


    for t in range(1,N):
        bottom_idx = arr[t].index(top) # 다음 밑 인덱스
        top_idx = match[bottom_idx] # 다음 위 인덱스
        bottom = arr[t][bottom_idx]
        top = arr[t][top_idx]
        next_max = 0
        for b in range(6):
            if b != bottom_idx and b != top_idx:
                if arr[t][b] > next_max:
                    next_max = arr[t][b]
        initial_max += next_max

    adds.append(initial_max)

result = max(adds)

print(result)








