first_array = map(str,input().split())
first_arr = [list(map(int,input().split())) for _ in range(2)]
second_array = map(str,input().split())
second_arr = [list(map(int,input().split())) for _ in range(2)]

multiple_arr = [[0] * 4 for _ in range(2)]
for i in range(2):
    for j in range(4):
        multiple_arr[i][j] = (first_arr[i][j]) * (second_arr[i][j])

for i in range(2):
    for j in range(4):
        print(multiple_arr[i][j], end=" ")
    print()