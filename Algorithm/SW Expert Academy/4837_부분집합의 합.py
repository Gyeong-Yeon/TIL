T = int(input())

for tc in range(1):
    N, K = map(int,input().split()) # N: 원소의 수, K: 부분 집합의 합
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]

    for i in range(1<<12): # 1<<N: 부분 집합의 개수
        for j in range(13): # 원소의 수만큼 비트를 비교함
            if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
                print(arr[j], end=", ")
        print()
    print()

