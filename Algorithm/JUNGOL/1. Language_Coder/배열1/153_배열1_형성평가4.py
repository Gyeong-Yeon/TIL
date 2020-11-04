arr = list(map(int,input().split()))

l = len(arr)

if l < 4:
    for i in range(l-1):
        print(arr[i], end=" ")
else:
    for i in range(l-4,l-1):
        print(arr[i], end=" ")