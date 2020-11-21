H = [] # 난쟁이들의 키
for h in range(9):
    H.append(int(input()))

find = sum(H) - 100

for i in range(len(H)-1):
    for j in range(i+1, len(H)):
        if H[i] + H[j] == find:
            H.remove(H[j])
            H.remove(H[i])
            break
    else:
        continue
    break

H.sort()

for i in H:
    print(i)