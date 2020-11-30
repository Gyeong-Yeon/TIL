N = int(input())
arr = list(map(int,input().split()))


up = [1]
down = [1]
equal = [1]
plus = 1
minus = 1
same = 1
for i in range(N-1):
    if arr[i+1] > arr[i]: # 증가
        plus += 1
        minus = 1
        same = 1
    elif arr[i+1] < arr[i]: # 감소
        plus = 1
        minus += 1
        same = 1
    else: # 동등
        plus += 1
        minus += 1
        same += 1
    up.append(plus)
    down.append(minus)
    equal.append(same)

result = 0
if max(up) > max(down):
    result = max(up)
else:
    result = max(down)

print(result)







