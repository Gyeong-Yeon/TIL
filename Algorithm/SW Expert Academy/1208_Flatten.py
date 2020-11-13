import sys
sys.stdin = open('input_flatten.txt')

for tc in range(1,11):
    N = int(input())
    box = list(map(int,input().split()))

    for i in range(N):
        x = box.index(max(box))
        y = box.index(min(box))

        box[x] -= 1
        box[y] += 1

    result = max(box) - min(box)

    print("#{} {}".format(tc, result))