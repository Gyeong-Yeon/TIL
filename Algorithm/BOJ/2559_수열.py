N, K = map(int,input().split())
tem = list(map(int,input().split()))

initial = 0
for i in range(K):
    initial += tem[i]

total = [initial]

next = 0
for i in range(K, N):
    next = initial + tem[i] - tem[i-K]
    total.append(next)
    initial = next

result = max(total)

print(result)

