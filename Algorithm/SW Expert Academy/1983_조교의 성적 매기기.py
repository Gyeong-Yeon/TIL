T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split()) # N: 학생수, K: 학생의 번호
    scores = [0]
    grade = {}
    for _ in range(N): # 학생들의 점수 입력받기
        M, F, H = map(int,input().split())
        # M: 중간, F: 기말, H: 과제
        total = (M * 0.35) + (F * 0.45) + (H * 0.20)
        scores.append(total)

    print(scores)