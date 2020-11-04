arr = list(map(str,input().split()))

alpha = {}
num = 65
for i in range(26): # value 값이 0인 알파벳 딕셔너리 만들기
    alpha[str(chr(num+i))] = 0

for i in range(len(arr)): # 딕셔너리에 카운트 하기
    if arr[i] in alpha:
        alpha[arr[i]] += 1
    else:
        break

num = 65
for i in range(26):
    if alpha[str(chr(num+i))] > 0:
        print("{} : {}".format(chr(num+i), alpha[str(chr(num+i))]))





