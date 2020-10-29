input_li = list(map(int,input().split()))

i = 0
sum = 0
cnt = 0


for i in range(len(input_li)):
    sum += input_li[i]
    cnt += 1
    if input_li[i] >= 100:
        break

avg = sum / cnt

print(sum)
print("%0.1f" % (avg))