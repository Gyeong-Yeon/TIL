N, K = map(int,input().split()) # N: 줄 수, K: 한방 최대 인원

girls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
boys = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for _ in range(N):
    S, Y = map(int,input().split()) # S: 성별, Y: 학년
    if S == 0: # 여학생인 경우
        girls[Y] += 1
    else: # 남학생인 경우
        boys[Y] += 1

g = 0 # 여학생 방 갯수
for i in range(1, 7):
    if girls[i] != 0:
        if girls[i] % K == 0: # 최대 인원의 배수인 경우
            g += (girls[i] // K)
        else: # 최대 인원 배수가 아닌 경우
            g += (girls[i] // K) + 1

b = 0 # 남학생 방 갯수
for i in range(1, 7):
    if boys[i] != 0:
        if boys[i] % K == 0:
            b += (boys[i] // K)
        else: # 최대 인원 배수가 아닌 경우
            b += (boys[i] // K) + 1

room = g + b
print(room)