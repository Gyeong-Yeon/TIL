n = int(input())
scores = list(map(int,input().split()))

avg = sum(scores) / n
print("avg : %0.1f" % avg)
if avg >= 80:
    print('pass')
else:
    print('fail')