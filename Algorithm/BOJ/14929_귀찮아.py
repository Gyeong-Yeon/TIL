n = int(input())
x = list(map(int,input().split()))

total = sum(x)
result = 0
for i in range(n):
    result += (total - x[i]) * x[i]

print(int(result / 2))
