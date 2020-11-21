N = int(input()) # 라운드 수

for _ in range(N):
    ta = {1: 0, 2: 0, 3: 0, 4: 0}
    tb = {1: 0, 2: 0, 3: 0, 4: 0}
    tag_a = list(map(int,input().split())) # A의 딱지
    tag_b = list(map(int,input().split())) # B의 딱지

    for i in range(1, tag_a[0]+1):
        ta[tag_a[i]] += 1
    for i in range(1, tag_b[0]+1):
        tb[tag_b[i]] += 1

    r = 4
    for i in range(4,0,-1):
        if ta[i] != tb[i]:
            if ta[i] > tb[i]:
                winner = 'A'
            else:
                winner = 'B'
            break
        else:
            r -= 1
            if r == 0:
                winner = 'D'

    print(winner)



