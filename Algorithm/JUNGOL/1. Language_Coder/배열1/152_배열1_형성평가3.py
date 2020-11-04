arr = [0] + list(map(int,input().split()))

odd_sum = 0
even_sum = 0
for i in range(1,11):
    if i % 2 != 0:
        odd_sum += arr[i]
    else:
        even_sum += arr[i]

print("odd : {}".format(odd_sum))
print("even : {}".format(even_sum))
