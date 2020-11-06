input()
first_arr = [list(map(int,input().split())) for _ in range(2)]
input()
second_arr = [list(map(int,input().split())) for _ in range(2)]


for i in range(2):
    for j in range(3):
        mul = first_arr[i][j] * second_arr[i][j]
        print(mul, end=" ")
    print()
