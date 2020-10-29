arr = [0] * 10

for i in range(10):
    arr[i] = int(input())

for _ in range(10):
    print(arr.pop(0), end=" ")


