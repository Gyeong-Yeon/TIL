n = int(input())

for i in range(n,0,-1):
    result = '*' * i
    print(result)
    if i == 1:
        for i in range(1,n+1):
            result = '*' * i
            print(result)
