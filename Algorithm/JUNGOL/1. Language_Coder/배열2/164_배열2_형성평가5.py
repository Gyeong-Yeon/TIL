sum_list = [0]

for i in range(1,5):
    print("{}class?".format(i), end=" ")
    scores = list(map(int,input().split()))
    sum_list.append(sum(scores))

for i in range(1,5):
    print("{}class : {}".format(i, sum_list[i]))
