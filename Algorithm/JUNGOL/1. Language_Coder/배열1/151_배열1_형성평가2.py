arr = [0] + list(map(int,input().split()))

sum = 0
for i in range(6):
    if i % 2 != 0:
        sum += arr[i]

print(sum)
