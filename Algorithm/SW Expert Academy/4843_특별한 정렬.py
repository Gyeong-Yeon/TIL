T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    arr.sort()

    max_li = []
    for i in range(N-1,N//2-1,-1): # 큰 값 순서대로 넣기
        max_li.append(arr[i])

    min_li = []
    for i in range(N//2):  # 작은 값 순서대로 넣기
        min_li.append(arr[i])

    new_arr = [] # 새로운 배열 채우기
    for i in range(N//2):
        new_arr.append(max_li[i])
        new_arr.append(min_li[i])

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(new_arr[i], end=" ")
    print()







