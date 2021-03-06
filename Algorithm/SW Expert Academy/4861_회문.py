T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]

    mid = M//2
    result = ''

    if M % 2 != 0: # M이 홀수일 때
        for i in range(N):  # 가로 확인
            for j in range(mid, N-mid):
                peri = 0
                for t in range(1, mid+1):
                    if arr[i][j-t] == arr[i][j+t]:
                        peri += 1
                if peri == mid:
                    result = ''.join(arr[i][j-mid:j+mid])

        for i in range(mid, N - mid):  # 세로 확인
            for j in range(N):
                peri = 0
                col = []
                for t in range(1, mid + 1):
                    if arr[i-t][j] == arr[i+t][j]:
                        peri += 1
                if peri == mid:
                    for b in range(-mid+1,mid+1):
                        col.append(arr[i+b][j])
                    result = ''.join(col)


    else: # M이 짝수일 때
        for i in range(N): # 가로 확인
            for j in range(mid-1,N-mid):
                peri = 0
                for t in range(1,mid+1):
                    if arr[i][j+1-t] == arr[i][j+t]:
                        peri += 1
                if peri == mid:
                    result = ''.join(arr[i][j+1-mid:j+mid+1])

        for i in range(mid-1,N-mid): # 세로 확인
            for j in range(N):
                peri = 0
                col = []
                for t in range(1,mid+1):
                    if arr[i+1-t][j] == arr[i+t][j]:
                        peri += 1
                if peri == mid:
                    for b in range(-mid+1, mid + 1):
                        col.append(arr[i + b][j])
                    result = ''.join(col)

    print("#{} {}".format(tc, result))


