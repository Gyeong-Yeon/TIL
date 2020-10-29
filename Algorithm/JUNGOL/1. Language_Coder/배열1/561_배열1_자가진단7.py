arr = list(map(int,input().split()))

max = 1
min = 9999
for i in range(10):
    if arr[i] < 100: # 100의 미만의 수
        if arr[i] > max:
            max = arr[i]
    else: # 100 이상의 수
        if arr[i] < min:
            min = arr[i]

print("%d %d" % (max, min))