N = int(input())
arr = [0] + list(map(int,input().split()))

order = []
for i in range(1, N+1):
    order = order[:len(order)-arr[i]] + [i] + order[len(order)-arr[i]:]

for i in range(N):
    print(order[i], end=" ")