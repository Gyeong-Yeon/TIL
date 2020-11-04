arr = list(map(int,input().split()))

sum = 0
cnt = 0
for i in range(100):
    if arr[i] == 0:
        break

    if arr[i] % 5 == 0:
        sum += arr[i]
        cnt += 1

avg = round(sum/cnt,1)

print("Multiples of 5 : {}".format(cnt))
print("sum : {}".format(sum))
print("avg : {}".format(avg))