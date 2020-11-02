T = int(input())
for t in range(1,T+1):
    N = int(input())
    garden = [list(map(int,input())) for _ in range(N)]

    mid = N//2
    sum = 0
    for i in range(N):
        if i <= mid: # 중간행까지
            for j in range(mid-i,mid+i+1):
                sum += garden[i][j]
        else: # 중간행+1부터 마지막행까지
            for j in range(i-mid,N-(i-mid)):
                sum += garden[i][j]

    print(f'#{t} {sum}')

