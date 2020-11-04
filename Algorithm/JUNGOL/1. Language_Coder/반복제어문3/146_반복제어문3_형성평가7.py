n = int(input())

str = 65
num = 0
for i in range(n,0,-1):
    for j in range(n):
        if j < i:
            result = chr(str)
            str += 1
        else:
            result = num
            num += 1
        print(result, end=" ")
    print()
