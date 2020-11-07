# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     cards = list(map(int,input()))
#
#     count = {} # 카드 갯수 카운트할 딕셔너리
#     for i in range(N):
#         count[cards[i]] = 0
#         if count[cards[i]] in count.keys(): # 중복되는 것 없게
#             continue
#
#     for i in range(N): # 카드 갯수 카운트
#         count[cards[i]] += 1
#
#     max_value = 0
#     max_key = 0
#     for key, value in count.items():
#         if value > max_value and key> max_key:
#             max_value = value
#             max_key = key
#
#     print("#{} {} {}".format(tc, max_key, max_value))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cards = int(input())
    numbers = list(map(int,input()))

    li_cnt = [0] * 10
    for n in numbers:
        li_cnt[n] += 1

    max_cnt = 0
    max_num = 0
    for i in range(len(li_cnt)):
        if li_cnt[i] >= max_cnt:
            max_cnt = li_cnt[i]
            max_num = i

    print(f'#{test_case} {max_num} {max_cnt}')










