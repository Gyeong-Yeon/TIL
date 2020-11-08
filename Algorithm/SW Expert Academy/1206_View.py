for tc in range(1,11):
    N = int(input())
    buildings = list(map(int,input().split()))

    view = 0
    for i in range(2,N-2):
        l1 = buildings[i] - buildings[i-1]
        l2 = buildings[i] - buildings[i-2]
        r1 = buildings[i] - buildings[i+1]
        r2 = buildings[i] - buildings[i+2]
        views = []
        if l1 > 0 and l2 > 0 and r1 > 0 and r2 > 0:
            views.append(l1)
            views.append(l2)
            views.append(r1)
            views.append(r2)
            view += min(views)

    print("#{} {}".format(tc, view))
