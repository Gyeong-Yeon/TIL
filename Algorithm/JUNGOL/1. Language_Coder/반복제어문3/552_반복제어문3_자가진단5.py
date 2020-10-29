n = int(input())

for i in range(n,0,-1):
    # space = " " * (n-i)
    result = '*' * ((2*i)-1)
    # print(space+result+space)
    print(result.center(2*n-1,' '))