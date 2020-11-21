C, R = map(int,input().split()) # C: 열, R: 행

N = int(input())

r_li = [0] # 행 리스트
c_li = [0] # 열 리스트
for _ in range(N):
    d, r = map(int,input().split())
    if d == 0:
        r_li.append(r)
    else:
        c_li.append(r)

r_li.sort()
r_li.append(R)
c_li.sort()
c_li.append(C)

r_max = 0
for i in range(1,len(r_li)):
    if r_li[i] - r_li[i-1] > r_max:
        r_max = r_li[i] - r_li[i-1]

c_max = 0
for i in range(1,len(c_li)):
    if c_li[i] - c_li[i-1] > c_max:
        c_max = c_li[i] - c_li[i-1]

result = r_max * c_max

print(result)


