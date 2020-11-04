n = int(input())
scores = list(map(int,input().split()))

# scores.sort(reverse=True)

for i in range(n-1,0,-1):
    for j in range(i):
        if scores[j] < scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]

for i in range(n):
    print(scores[i])