n = int(input())

num = 1
for i in range(n):
    for j in range(n):
        print(num, end=" ")
        if num < 9:
            num += 2
        else:
            num = 1
    print()

