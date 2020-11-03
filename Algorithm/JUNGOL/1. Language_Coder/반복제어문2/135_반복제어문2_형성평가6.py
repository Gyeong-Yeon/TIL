S, E = map(int,input().split())

if S > E:
    S, E = E, S

sum = 0
cnt = 0
for i in range(S,E+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        cnt += 1

print("sum : %d" % sum)
print("avg : %0.1f" % (sum/cnt))