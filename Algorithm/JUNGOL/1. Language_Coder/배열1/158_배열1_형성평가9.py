arr = list(map(int,input().split()))

print(len(arr)-1)
for i in range(100):
    if arr[i] == 0:
        break

    if arr[i] % 2 != 0:
        result = arr[i] * 2
    else:
        result = arr[i] // 2

    print(result,end=" ")



