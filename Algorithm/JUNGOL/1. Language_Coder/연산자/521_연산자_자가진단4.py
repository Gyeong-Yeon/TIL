N, M = map(int,input().split())
cal = [N+1, M-1, (N)*(M-1)]

for i in range(len(cal)):
    print(cal[i], end=" ")