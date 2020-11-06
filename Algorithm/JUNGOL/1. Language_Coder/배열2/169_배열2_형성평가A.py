arr = [list(map(ord,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(5):
        result = chr(arr[i][j]+32)
        print(result, end=" ")
    print()