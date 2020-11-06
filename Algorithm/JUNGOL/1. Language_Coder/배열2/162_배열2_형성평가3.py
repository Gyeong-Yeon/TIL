arr = list(map(int,input().split())) + [0] * 8

for i in range(2,10):
    arr[i] = (arr[i-2] + arr[i-1]) % 10

print(*arr)


