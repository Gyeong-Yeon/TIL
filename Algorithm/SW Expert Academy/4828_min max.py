T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    min = 1000001
    for i in range(N):
        if arr[i] < min:
            min = arr[i]

    max = 0
    for i in range(N):
        if arr[i] > max:
            max = arr[i]

    result = max - min

    print("#{} {}".format(tc, result))
