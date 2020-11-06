arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]

sum = 0
for i in range(4):
    for j in range(3):
        sum += arr[i][j]
        print(arr[i][j], end=" ")
    print()
print(sum)
