N, M = map(int,input().split())

if N < M:
    N, M = M, N

quo = N // M
rest = N % M

print("%d / %d = %d...%d" % (N,M,quo,rest))