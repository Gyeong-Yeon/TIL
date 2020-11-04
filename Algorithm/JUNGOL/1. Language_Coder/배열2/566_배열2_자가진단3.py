n = int(input())

arr = [100, n] # 초기 배열

# for i in range(100):
#     minus = arr[i] - arr[i+1]
#     arr.append(minus)
#     if minus < 0:
#         break
#
# for i in range(len(arr)):
#     print(arr[i], end=" ")

while arr[-1] > 0:
    arr.append(arr[-2] - arr[-1])
print(*arr)
