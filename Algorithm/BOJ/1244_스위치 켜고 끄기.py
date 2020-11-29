S = int(input()) # 스위치 개수
switch = list(map(int,input().split())) # 각 스위치의 상태
N = int(input()) # 학생수

for _ in range(N):
    G, C = map(int,input().split()) # G: 성별, C: 받은 수
    if G == 1: # 남학생인 경우,
        for g in range(C,S+1,C):
            # (애초범위는 1부터 S까지 인데, C의 배수만 봐야하니까 C씩 건너뛰면서 순회)
            if switch[g-1] == 1: # 1이면
                switch[g-1] = 0 # 0으로 바꿔주고
            else: # 0이면
                switch[g-1] = 1 # 1로 바꿔준다.
    else: # 여학생인 경우,
        min = 0 # 받은 수 기준으로 순회가능한 편도 범위
        left = C - 1
        right = S - C
        if left < right:
            min = left
        else:
            min = right

        cnt = 0
        for d in range(1,min+1): # 대칭 범위 찾기
            if switch[C-1-d] == switch[C-1+d]:
                cnt += 1
            else:
                break

        for i in range(C-cnt,C+cnt+1):
            if switch[i-1] == 1:  # 1이면
                switch[i-1] = 0  # 0으로 바꿔주고
            else:  # 0이면
                switch[i-1] = 1  # 1로 바꿔준다.

if len(switch) > 20:
    row = len(switch) // 20
    col = len(switch) % 20
    for i in range(row+1):
        if i < row:
            for j in range(20):
                print(switch[(20*i)+j], end=" ")
        else:
            for j in range(col):
                print(switch[(20*i)+j], end=" ")
        print()
else:
    print(*switch)

