arr = ['J', 'U', 'N', 'G', 'O', 'L']

input_str = str(input())

for i in range(len(arr)):
    if arr[i] == input_str:
        result = arr.index(input_str)
    else:
        reuslt = 'none'

print(reuslt)