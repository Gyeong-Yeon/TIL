N, M = map(int,input().split())

if N*M:
    mul = 1
else:
    mul = 0

if N+M:
    add = 1
else:
    add = 0

cal = [mul, add]

print("%d %d" % (mul, add))