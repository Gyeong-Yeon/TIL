input_arr = list(map(int,input().split()))

arr = [0] * 100

for i in range(len(input_arr)):
    arr[i] = input_arr[i]

for i in range(99,-1,-1):
    if arr[i] != 0:
        print(arr[i], end=" ")
