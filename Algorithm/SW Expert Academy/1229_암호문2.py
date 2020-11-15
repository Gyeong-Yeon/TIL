import sys
sys.stdin = open('input_암호문2.txt')

for tc in range(1, 11):
    N = int(input()) # 원본 암호문 길이
    password = list(map(int,input().split())) # 원본 암호문
    M = int(input()) # 명령어 개수
    arr = list(map(str,input().split())) # 명령어 1차배열

    com = [list() for _ in range(M)] # 명령어 2차배열
    i = 0
    while i < M:
        for a in range(len(arr)): # 1차배열로 입력받은 명령어 반복
            if arr[a] == 'I': # 삽입인 경우
                com[i].append(arr[a]) # I
                com[i].append(int(arr[a+1])) # x
                com[i].append(int(arr[a+2])) # y
                for t in range(1,int(arr[a+2])+1): # s
                    com[i].append(int(arr[a+2+t]))
                i += 1
            elif arr[a] == 'D': # 삭제인 경우
                com[i].append(arr[a]) # D
                com[i].append(int(arr[a+1])) # x
                com[i].append(int(arr[a+2])) # y
                i += 1

    for i in range(M):
        if com[i][0] == 'I':
            password = password[:com[i][1]] + com[i][3:] + password[com[i][1]:]
        elif com[i][0] == 'D':
            password = password[:com[i][1]] + password[com[i][1]+com[i][2]:]

    print("#{}".format(tc), end=" ")
    for p in range(10):
        print(password[p], end=" ")
    print()


