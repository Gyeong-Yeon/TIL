arr = list(map(int,input().split()))

sum = 0
cnt = 0
for i in range(20):
    if arr[i] == 0:
        break
    sum += arr[i]
    cnt += 1

avg = int(sum/cnt)

print(f'{sum} {avg}')
