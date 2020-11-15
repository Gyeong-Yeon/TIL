import sys
sys.stdin = open('input_암호문3.txt')

for tc in range(1, 11):
    N = int(input())
    password = list(map(int,input().split()))
    M = int(input())
    arr = list(map(str,input().split()))

    com = [list() for _ in range(M)]
    i = 0
    while i < M:
        for a in range(len(arr)):
            if arr[a] == 'I': # 삽입
                com[i].append(arr[a]) # I
                com[i].append(int(arr[a+1])) # x
                com[i].append(int(arr[a+2])) # y
                for t in range(1, int(arr[a+2])+1): # s
                    com[i].append(int(arr[a+2+t]))
                i += 1
            elif arr[a] == 'D': # 삭제
                com[i].append(arr[a]) # D
                com[i].append(int(arr[a+1])) # x
                com[i].append(int(arr[a+2])) # y
                i += 1
            elif arr[a] == 'A': # 추가
                com[i].append(arr[a]) # A
                com[i].append(int(arr[a+1])) # y
                for t in range(1, int(arr[a+1])+1): # s
                    com[i].append(int(arr[a+1+t]))
                i += 1

    for i in range(M):
        if com[i][0] == 'I':
            password = password[:com[i][1]] + com[i][3:] + password[com[i][1]:]
        elif com[i][0] == 'D':
            password = password[:com[i][1]] + password[com[i][1]+com[i][2]:]
        if com[i][0] == 'A':
            password = password + com[i][2:]

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(password[i], end=" ")
    print()



