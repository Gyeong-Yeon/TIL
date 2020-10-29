n = int(input())
input_li = list(map(int,input().split()))

sum = 0
for i in range(n):
    sum += input_li[i]

avg = sum / n

print("%0.2f" % avg)