T = int(input())
for t in range(1,T+1):
    a, b = map(int,input().split()) # a:첫번째 리스트 길이, b:두번째 리스트 길이
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if a > b: # 첫번째 리스트 길이가 더 길면, SWAP
        A, B = B, A # 첫번째 리스트가 두번째 리스트보다 길이가 짧음

    sum_list = []
    for i in range(len(B)-len(A)+1): # 리스트 B의 시작점 순회하면서
        new_B = B[i:i+a] # 리스트 A 길이만큼 새로운 리스트 B 생성
        sum_ = 0
        for j in range(len(A)):
            sum_ += A[j] * new_B[j]
        sum_list.append(sum_)

    result = max(sum_list)

    print(f'#{t} {result}')










