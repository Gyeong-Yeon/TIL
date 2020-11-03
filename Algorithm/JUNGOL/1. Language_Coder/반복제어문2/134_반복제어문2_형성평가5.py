arr = list(map(int,input().split()))

even_cnt = 0
odd_cnt = 0
for i in range(10):
    if arr[i] % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print("even : %d" % even_cnt)
print("odd : %d" % odd_cnt)