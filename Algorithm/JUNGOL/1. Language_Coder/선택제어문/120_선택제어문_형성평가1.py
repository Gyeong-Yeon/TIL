N, M = map(int,input().split())

if N > M:
    N, M = M, N

print(M-N)