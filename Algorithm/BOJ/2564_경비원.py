R, C = map(int,input().split()) # 가로, 세로
N = int(input()) # 상점의 개수

distance = []
for _ in range(N+1): # 상점 위치
    D, F = map(int,input().split()) # 방향, 거리
    # 1: 북, 2: 남, 3: 서, 4: 동
    if D == 1:
        d = F
    elif D == 2:
        d = R + C + (R-F)
    elif D == 3:
        d = R + C + R + (C-F)
    else:
        d = R + F
    distance.append(d)

total = []
for i in range(N):
    gap = 0
    if distance[i] < distance[N]:
        if (distance[N] - distance[i]) < 2*(R+C) - (distance[N] - distance[i]):
            gap = (distance[N] - distance[i])
        else:
            gap = 2*(R+C) - (distance[N] - distance[i])
    else:
        if (distance[i] - distance[N]) < 2*(R+C) - (distance[i] - distance[N]):
            gap = (distance[i] - distance[N])
        else:
            gap = 2*(R+C) - (distance[i] - distance[N])
    total.append(gap)

result = sum(total)

print(result)

