arr = list(map(int,input().split()))

max = 0
min = 10000
for i in range(10):
    if arr[i] < 100: # 100의 미만의 수
        if arr[i] > max:
            max = arr[i]
    else: # 100 이상의 수
        if arr[i] < min:
            min = arr[i]

if max == 0:
    max = 100
elif min == 10000:
    min = 100

print("%d %d" % (max, min))