A, B, C = map(int,input().split())

if A > B and A > C:
    big = 1
else:
    big = 0

if A == B == C:
    com = 1
else:
    com = 0

print("%d %d" % (big, com))
