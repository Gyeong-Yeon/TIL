n = int(input())

for i in range(n,0,-1):
    #space = " " * (n-i)
    result = '*' * i
    #print(space+result)
    print(result.rjust(n,' '))