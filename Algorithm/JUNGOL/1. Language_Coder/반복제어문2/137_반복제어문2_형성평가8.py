r, c = map(int,input().split())

for i in range(1,r+1):
    for j in range(c):
        result = i + i*j
        print(result, end=" ")
    print()