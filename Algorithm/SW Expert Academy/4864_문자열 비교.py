T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    str1_l = len(list(str1))
    str2_l = len(list(str2))

    for i in range(str2_l-str1_l+1):
        if str2[i:i+str1_l] == str1:
            result = 1
            break
        else:
            result = 0

    print("#{} {}".format(tc, result))


