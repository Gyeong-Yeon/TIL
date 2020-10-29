input_li = list(map(int,input().split()))

odd_cnt = 0
even_cnt = 0

for i in range(len(input_li)):
    if input_li[i] == 0:
        break

    if (input_li[i] % 2) > 0: # 홀수
        odd_cnt += 1
    else: # 짝수
        even_cnt += 1

print(f'odd : {odd_cnt}')
print(f'even : {even_cnt}')