arr = [list(map(int,input().split())) for _ in range(4)]

for i in range(4):
    row_avg = sum(arr[i]) / 2
    print(int(row_avg), end=" ")
print()

for i in range(2):
    col_sum = 0
    for j in range(4):
        col_sum += arr[j][i]
    col_avg = col_sum / 4
    print(int(col_avg), end=" ")
print()

total = 0
for i in range(4):
    for j in range(2):
        total += arr[i][j]

total_avg = total / 8
print(int(total_avg))
