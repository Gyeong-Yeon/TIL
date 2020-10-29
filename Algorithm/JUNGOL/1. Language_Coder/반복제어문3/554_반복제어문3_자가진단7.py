n = int(input())

num = 1
alp = 0
for i in range(n,0,-1):
    for j in range(n+1):
        if j < i:
            result = num
            print(result, end=" ")
            num += 1
        else:
            result = chr(int(65+alp))
            print(result, end=" ")
            alp += 1
    print()

