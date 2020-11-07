T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    # K: 최대 이동 거리/충전, N: 정류장 번호, M: 정류장 개수
    stations = list(map(int,input().split()))

    cnt = 0
    w = 0 + K # 전기버스 위치
    back = 0

    while w < N:
        if w in stations:
            w += K
            cnt += 1
            back = 0
        else:
            if back < K-1:
                w -= 1
                back += 1
            else:
                cnt = 0
                break

    print("#{} {}".format(tc, cnt))




