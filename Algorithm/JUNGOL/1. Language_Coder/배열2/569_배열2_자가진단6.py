
cnt = 0

for _ in range(5):
    K, E, M, S = map(int,input().split())
    sum = K + E + M + S
    avg = sum / 4
    if avg >= 80:
        print('pass')
        cnt += 1
    else:
        print('fail')

print(f'Successful : {cnt}')


