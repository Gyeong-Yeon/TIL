T = int(input())

for t in range(1,T+1):
    # calender = list(map(str,input())) # join함수로 원소들을 추출하기 위해 입력값을 str형태로 list에 넣는다.
    # YYYY = ''.join(calender[:4]) # 년
    # MM = ''.join(calender[4:6]) # 월
    # DD = ''.join(calender[6:8]) # 일
    #
    # if MM == '01' or MM == '03' or MM == '05' or MM == '07' or MM == '08' or MM == '10' or MM == '12':
    #     if 1 <= int(DD) <= 31:  # 날짜가 31일까지인 달
    #         print(f'#{t} {YYYY}/{MM}/{DD}')
    #     else:
    #         print(f'#{t} -1')
    # elif MM == '04' or MM == '06' or MM == '09' or MM == '11':
    #     if 1 <= int(DD) <= 30:  # 날짜가 30일까지인 달
    #         print(f'#{t} {YYYY}/{MM}/{DD}')
    #     else:
    #         print(f'#{t} -1')
    # elif MM == '02':
    #     if 1 <= int(DD) <= 28:  # 날짜가 28일까지인 달
    #         print(f'#{t} {YYYY}/{MM}/{DD}')
    #     else:
    #         print(f'#{t} -1')
    # else:
    #     print(f'#{t} -1')

    calender = input()
    year = calender[:4]
    month = calender[4:6]
    day = calender[6:9]

    flag = 1
    if int(month) < 1 or int(month) > 12:
        flag = -1

    if int(month) == 2:
        if int(day) > 28:
            flag = -1
    elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        if int(day) > 30:
            flag = -1
    else:
        if int(day) > 31:
            flag = -1

    if flag == -1:
        print("#{} -1".format(t))
    else:
        print("#{} {}/{}/{}".format(t,year,month,day))






