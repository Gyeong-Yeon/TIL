N = int(input())

i = 0
while N <= 100:
    result = N + (N*i)
    if result >= 100:
        break
    print(result, end=" ")
    if result % 10 == 0:
        break
    i += 1




