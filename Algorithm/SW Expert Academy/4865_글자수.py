T = int(input())

for tc in range(1,T+1):
    str1 = list(map(str,input()))
    str2 = list(map(str,input()))

    count = {}
    for i in range(len(str1)):
        count[str1[i]] = 0
        if count[str1[i]] in count.keys():
            continue

    for i in range(len(str2)):
        if str2[i] in count.keys():
            count[str2[i]] += 1

    max = 0
    for value in count.values():
        if value > max:
            max = value

    print("#{} {}".format(tc, max))
