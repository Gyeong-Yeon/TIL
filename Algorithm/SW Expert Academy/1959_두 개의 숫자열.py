T = int(input())
for t in range(1,T+1):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if len(A) > len(B):
        A, B = B, A

    sum_list = []
    for b in range(len(B)-len(A)+1):
        new_B = B[b:b+len(A)]
        sum = 0
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j:
                    sum += A[i] * new_B[j]
        sum_list.append(sum)

    result = max(sum_list)

    print(f'{t} {result}')










