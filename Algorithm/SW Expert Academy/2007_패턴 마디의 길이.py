T = int(input())

for tc in range(1, T+1):
    pattern = input()

    cnt = 1
    first = pattern[0]
    for i in range(1,30):
        if pattern[i] != first:
            cnt += 1
        elif pattern[i] == first and pattern[i+1] != pattern[1]:
            cnt += 1
        else:
            break

    print("#{} {}".format(tc, cnt))

