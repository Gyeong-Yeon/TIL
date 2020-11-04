n = int(input())

l = n*2 -1

for i in range(l,0,-2):
    result = '*'*i
    print(result.center(l, ' '))

for i in range(3,l+1,2):
    result = '*'*i
    print(result.center(l, ' '))