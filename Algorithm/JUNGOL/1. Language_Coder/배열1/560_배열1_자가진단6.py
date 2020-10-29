arr = list(map(int,input().split()))

min = 99999999999
for i in range(10):
    if arr[i] < min:
        min = arr[i]

print(min)
