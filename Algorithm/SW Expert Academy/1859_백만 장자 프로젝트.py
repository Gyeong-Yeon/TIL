T = int(input())

for tc in range(1,T+1):
    N = int(input())
    days = list(map(int,input().split()))

    buy = 0
    buy_cnt = 0
    sell = 0
    for i in range(N-1):
        if days[i] <= days[i+1]:
            buy += days[i]
            buy_cnt += 1
            if max(days) == days[N-1]:
                sell += days[N-1] * buy_cnt
            elif days[i] > days[i+1]:
                sell += days[i] * buy_cnt
    result = sell - buy
    print(result)

