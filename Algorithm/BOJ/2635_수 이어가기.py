N = int(input())

max = 0
max_li = []
for i in range(N,0,-1):
    arr = [N]
    arr.append(i)

    result = 0
    while result >= 0:
        result = arr[-2] - arr[-1]
        if result >= 0:
            arr.append(result)


    if len(arr) > max:
        max = len(arr)
        max_li = arr

print(max)
print(*max_li)


