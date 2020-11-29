w, h = map(int, input().split()) # w: 가로, h: 세로
p, q = map(int, input().split()) # p: 첫 가로 좌표, q: 첫 세로 좌표
t = int(input()) # t: 시간

time_p = p + t # 첫 가로 좌표에서 쭉 오른쪽 45도로 갔을 경우
time_q = q + t # 첫 세로 좌표에서 쭉 오른쪽 45도로 갔을 경우

final_p = 0 # 최종 도착 p
if (time_p // w) % 2 == 0:
    final_p = 0 + (time_p % w)
else:
    final_p = w - (time_p % w)

final_q = 0 # 최종 도착 q
if (time_q // h) % 2 == 0:
    final_q = 0 + (time_q % h)
else:
    final_q = h - (time_q % h)

print("{} {}".format(final_p, final_q))