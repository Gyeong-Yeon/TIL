T = int(input())

for _ in range(T):
    tc = int(input())
    scores = list(map(int,input().split()))

    count = {} # 점수별 개수를 0으로 초기화한 딕셔너리 만들기
    for i in range(len(scores)):
        count[scores[i]] = 0
        if scores[i] in count.keys():
            continue

    for i in range(len(scores)): # 점수별 갯수 카운트 하기
        count[scores[i]] += 1

    max = 0
    for key, value in count.items(): # 카운트 딕셔너리에서 점수와 그 갯수를 확인하는데,
        if value > max:
            max = value # 최댓값인 갯수가 있을 때,
            result = key # 그 점수가 답

    print("#{} {}".format(tc, result))








