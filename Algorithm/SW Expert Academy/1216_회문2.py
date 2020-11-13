import sys
sys.stdin = open('input_회문2.txt')

def peri(arr):
    for p in range(100,0,-1): # arr
        for i in range(100):
            for j in range(100-p+1):
                if arr[i][j:j+p] == arr[i][j:j+p][::-1]:
                    return p

for _ in range(1,11):
    tc = int(input())
    arr = [input() for _ in range(100)]
    col_arr = [''.join(i) for i in zip(*arr)]

    p1 = peri(arr)
    p2 = peri(col_arr)

    result = 0
    if p1 > p2:
        result = p1
    else:
        result = p2

    print("#{} {}".format(tc, result))

