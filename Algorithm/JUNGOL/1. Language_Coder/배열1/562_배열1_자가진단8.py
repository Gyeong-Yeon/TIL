arr = [0] + list(map(int,input().split()))

sum_even = 0
sum_odd = 0
odd_cnt = 0
for i in range(1,11):
    if i % 2 == 0: # 짝수
        sum_even += arr[i]
    else:
        sum_odd += arr[i]
        odd_cnt += 1

print("sum : %d" % sum_even)
print("avg : %0.1f" % (sum_odd/odd_cnt))