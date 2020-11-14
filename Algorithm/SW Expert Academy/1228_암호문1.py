import sys
sys.stdin = open('input_암호문1.txt')

for tc in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
    M = int(input())
    li = list(map(str,input().split()))


    ins = [list() for _ in range(M)] # 명령어
    i = 0
    while i < M:
        for l in range(len(li)):
            if li[l] == 'I':
                ins[i].append(li[l])
                ins[i].append(int(li[l+1]))
                ins[i].append(int(li[l+2]))
                for t in range(1,int(li[l+2])+1):
                    ins[i].append(int(li[l+2+t]))
                i += 1

    for i in range(M):
        arr = arr[:ins[i][1]] + ins[i][3:] + arr[ins[i][1]:]

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(arr[i], end=" ")
    print()




