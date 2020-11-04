arr = list(map(int,input().split()))

dice = {}
for i in range(1,7):
    dice[i] = 0

for i in range(10):
    dice[arr[i]] += 1

for i in range(1,7):
    print("{} : {}".format(i,dice[i]))