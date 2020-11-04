arr = list(map(int,input().split()))

max = -1000
min = 1000

for i in range(100): # 최댓값
    if arr[i] == 999:
        break

    if arr[i] > max:
        max = arr[i]

for i in range(100): # 최솟값
    if arr[i] == 999:
        break

    if arr[i] < min:
        min = arr[i]

print("max : {}".format(max))
print("min : {}".format(min))
