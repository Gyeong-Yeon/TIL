N = int(input())

i = 1
sum = 0

for i in range(N+1):
    if i % 5 == 0:
        sum += i

print(sum)