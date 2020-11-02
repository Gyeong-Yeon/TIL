N = int(input())

n_list = []
for i in range(1,N+1):
    n_list.append(str(i))

for j in range(N):
    if '3' in n_list[j] or '6' in n_list[j] or '9' in n_list[j]: # 3이 포함되어 있는 경우
        cnt = n_list[j].count('3') + n_list[j].count('6') + n_list[j].count('9')
        n_list[j] = '-' * cnt
    print(n_list[j], end=" ")

