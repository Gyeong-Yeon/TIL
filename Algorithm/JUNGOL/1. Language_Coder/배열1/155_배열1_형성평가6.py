arr = ['J', 'U', 'N', 'G', 'O', 'L']

input_str = input()

for i in range(len(arr)):
    if input_str in arr:
        result = arr.index(input_str)
    else:
        result = 'none'

print(result)