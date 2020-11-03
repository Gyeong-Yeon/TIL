arr = list(map(int,input().split()))

cnt = 0
for i in range(len(arr)):
    if arr[i] % 3 != 0 and arr[i] % 5 != 0:
        cnt += 1

print(cnt)