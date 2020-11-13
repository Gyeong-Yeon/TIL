T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    # K: 최대 이동 거리/충전, N: 정류장 번호, M: 정류장 개수
    stations = list(map(int,input().split()))

    cnt = 0 # 충전 횟수
    w = 0 + K # 전기버스 위치
    back = 0 # 뒤로가는 정류장 갯수

    while w < N:
        if w in stations: # 0번에서 최대 이동 거리만큼 갔을 때, 충전기가 있으면
            w += K # 가는 동안 전기를 다 썼으니까 다시 충전 해주고,
            cnt += 1 # 충전 횟수 더해주기
            back = 0
        else: # 충전기가 없는 경우
            if back < K-1: # 뒤로가는 정류장 갯수가 K보다 작은 경우에만
                w -= 1 # 위치를 하나씩 빼준다
                back += 1 # 그리고 뒤로간 정류장 갯수를 늘리고
            else: # 뒤
                cnt = 0
                break

    print("#{} {}".format(tc, cnt))




