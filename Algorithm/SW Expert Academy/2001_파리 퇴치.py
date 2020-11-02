T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split()) # N:배열크기, M:파리채크기
    fly = [list(map(int,input().split())) for _ in range(N)] # 파리들 배열

    total = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for t in range(i,i+M):
                for b in range(j,j+M):
                    sum += fly[t][b]
            total.append(sum)

    result = max(total)

    print("#%d %d" % (tc, result))

