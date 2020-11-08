for _ in range(1,11):
    tc = int(input())
    str1 = input()
    str2 = input()

    l1 = len(list(str1))
    l2 = len(list(str2))

    cnt = 0
    for i in range(l2-l1+1):
        if str2[i:i+l1] == str1:
            cnt += 1

    print("#{} {}".format(tc, cnt))