input_arr = list(map(int,input().split()))

arr = []
for i in range(len(input_arr)): # 십의 자리 리스트 만들기
    if input_arr[i] != 0:
        arr.append(input_arr[i]//10)


ten = {}
for i in range(10): # 십의 자리 숫자 갯수 세는 딕셔너리 만들기
    ten[i] = 0

for i in range(len(arr)): # 십의 자리 숫자 세기
    ten[arr[i]] += 1

for i in range(10):
    if ten[i] > 0:
        print("{} : {}".format(i, ten[i]))

