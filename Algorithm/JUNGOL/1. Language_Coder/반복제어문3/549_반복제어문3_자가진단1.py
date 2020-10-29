n = int(input())

i = 1
sum = 0
cnt = 0
for i in range(n+1):
    if i % 2 != 0:
        sum += i
        cnt += 1
    if sum >= n:
        break

print(f'{cnt} {sum}')