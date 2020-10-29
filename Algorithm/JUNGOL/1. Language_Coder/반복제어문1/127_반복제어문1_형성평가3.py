input_li = list(map(int,input().split()))

sum = 0
cnt = 0

for i in range(len(input_li)):
    if input_li[i] < 0 or input_li[i] > 100:
        break

    sum += input_li[i]
    cnt += 1


avg = sum / cnt

print(f'sum : {sum}')
print("avg : %0.1f" % (avg))