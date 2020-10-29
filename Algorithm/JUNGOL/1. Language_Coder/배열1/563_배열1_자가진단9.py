arr = list(map(int,input().split()))
arr.sort(reverse=True)

for i in range(10):
    print(arr[i], end=" ")
