n = int(input())

cnt = 0
for i in range(n,0,-1):
    for _ in range(i):
        result = chr(int(65+cnt))
        print(result, end="")
        cnt += 1
    print()


