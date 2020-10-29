input_arr = list(map(int,input().split()))

arr = []
for i in range(len(input_arr)):
    if input_arr[i] != 0:
        arr.append(input_arr[i])

print(arr)

