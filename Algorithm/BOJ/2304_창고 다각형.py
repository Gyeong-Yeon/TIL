N = int(input())

r = [] # 기둥 위치 리스트
c = [] # 기둥 높이 리스트
for _ in range(N):
    L, H = map(int,input().split())
    r.append(L)
    c.append(H)

spot = sorted(r)
pillar = []
for i in range(N):
    h = c[r.index(spot[i])]
    pillar.append(h)
# spot = [2, 4, 5, 8, 11, 13, 15]
# pillar = [4, 6, 3, 10, 4, 6, 8]

top = pillar.index(max(pillar)) # 가장 높은 기둥 위치

area = max(pillar)
i = 0
j = 1
while j <= top:
    if pillar[j] >= pillar[i]:
        area += (spot[j] - spot[i]) * pillar[i]
        i = j
        j += 1
    else:
        j += 1

i = N - 2
j = N - 1
while i >= top:
    if pillar[i] >= pillar[j]:
        area += (spot[j] - spot[i]) * pillar[j]
        j = i
        i -= 1
    else:
        i -= 1

print(area)