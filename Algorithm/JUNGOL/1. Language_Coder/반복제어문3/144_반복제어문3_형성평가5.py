n = int(input())

l = 2*n - 1
for i in range(1,l+1,2):
    result = '*'*i
    print(result.rjust(l, ' '))