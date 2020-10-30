n = int(input())

num = 1
alp = 0
for i in range(n,0,-1):
    for j in range(n+1):
        if j < i:
            result = num
            num += 1
        else:
            result = chr(int(65+alp))
            alp += 1
        print(result, end=" ")
    print()

