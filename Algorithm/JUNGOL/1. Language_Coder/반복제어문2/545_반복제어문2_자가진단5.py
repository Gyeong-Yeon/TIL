arr = list(map(int,input().split()))

three = 0
for i in range(10):
    if arr[i] % 3 == 0:
        three += 1

five = 0
for i in range(10):
    if arr[i] % 5 == 0:
        five += 1


print("Multiples of 3 : %d" % three)
print("Multiples of 5 : %d" % five)