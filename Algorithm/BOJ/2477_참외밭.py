K = int(input()) # 평당 재배되는 참외 갯수

total = []
for _ in range(6):
    D, L = map(int,input().split()) # D: 방향, L: 거리
    # 1: 동쪽(오), 2: 서쪽(왼), 3: 남쪽(아래), 4: 북쪽(위)
    total.append(L)

max1 = 0
max1_idx = 0
for i in range(6):
    if total[i] > max1:
        max1 = total[i]
        max1_idx = i

max2 = 0
max2_idx = 0
if total[(max1_idx-1) % 6] > total[(max1_idx+1) % 6]:
    max2 = total[(max1_idx-1) % 6]
    max2_idx = (max1_idx-1) % 6

else:
    max2 = total[(max1_idx+1) % 6]
    max2_idx = (max1_idx+1) % 6

rest1 = total[(max1_idx+3) % 6]
rest2 = total[(max2_idx+3) % 6]

area = (max1*max2) - (rest1*rest2)

watermelon = K * area

print(watermelon)
