T = int(input())

for tc in range(1,T+1):
    P, A, B = map(int,input().split())

    s = 1
    e = P
    search_A = 0
    while True:
        c = int((s+e)/2)
        search_A += 1
        if c != A:
            if c < A:
                s = c
            else:
                e = c
        else:
            break

    s = 1
    e = P
    search_B = 0
    while True:
        c = int((s + e) / 2)
        search_B += 1
        if c != B:
            if c < B:
                s = c
            else:
                e = c
        else:
            break

    if search_A < search_B:
        result = 'A'
    elif search_A == search_B:
        result = 0
    else:
        result = 'B'

    print("#{} {}".format(tc, result))


