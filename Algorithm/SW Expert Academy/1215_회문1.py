import sys
sys.stdin = open('input_회문1.txt')

for tc in range(1,11):
    N = int(input())
    arr = [list(map(str,input())) for _ in range(8)]
    arr_col = [''.join(i) for i in zip(*arr)]

    mid = N // 2
    peri = 0

    if N % 2 != 0: # N이 홀수인 경우
        for i in range(8):
            for j in range(mid,8-mid):
                cnt = 0
                for t in range(1, mid+1):
                    if arr[i][j-t] == arr[i][j+t]:
                        cnt += 1
                if cnt == mid:
                    peri += 1

        for i in range(8):
            for j in range(mid,8-mid):
                cnt = 0
                for t in range(1, mid+1):
                    if arr_col[i][j-t] == arr_col[i][j+t]:
                        cnt += 1
                if cnt == mid:
                    peri += 1

    else: # N이 짝수인 경우
        for i in range(8):
            for j in range(mid-1,8-mid):
                cnt = 0
                for t in range(1, mid+1):
                    if arr[i][j+1-t] == arr[i][j+t]:
                        cnt += 1
                if cnt == mid:
                    peri += 1

        for i in range(8):
            for j in range(mid-1,8-mid):
                cnt = 0
                for t in range(1, mid+1):
                    if arr_col[i][j+1-t] == arr_col[i][j+t]:
                        cnt += 1
                if cnt == mid:
                    peri += 1

    print("#{} {}".format(tc, peri))


# import sys
# sys.stdin = open('input.txt')
#
# for t in range(1,11):
#     k = int(input())
#     box = [input() for _ in range(8)]
#     box_col = [''.join(x) for x in zip(*box)]
#
#     cnt=0
#     for i in range(8):
#         for j in range(0,9-k):
#             if box[i][j:j+k] == box[i][j:j+k][::-1]:
#                 cnt+=1
#             if box_col[i][j:j+k] == box_col[i][j:j+k][::-1]:
#                 cnt+=1
#
#     print('#{} {}'.format(t,cnt))
