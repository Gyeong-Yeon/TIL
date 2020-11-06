for tc in range(1, 11):
    # 공백 있어서 일단 문자열로 받음
    N, li = list(map(str, input().split()))

    # li를 arr(리스트)에 담음
    #(굳이 리스트로 담는 이유는 아래 pop 메소드가 리스트에서만 쓸 수 있어서)
    arr = list(li)

    i = 0 # 인덱스로 접근하기위해 i 변수설정

    while True:
        # 1)지금숫자랑 다음숫자랑 같으면
        if arr[i] == arr[i+1]:
            arr.pop(i) #지금숫자의 인덱스로 접근해서 값 삭제
            arr.pop(i) #다음숫자의 인덱스로 접근해서 값 삭제 (i+1이 아니라 i 인 이유, 앞에 숫자 삭제하면서 배열길이가 달라짐)

            # for~else문: 앞에서 같은거 두개 삭제하고 arr 리스트에 연속된 같은 숫자 있는지 확인하는 용도,
            for i in range(len(arr)-1): #순회해서
                if arr[i] == arr[i+1]: #같은숫자나오면 break하고  for문에서 빠져나와서 34번째줄로감
                    break
            else: # 위에 for문 다 순회해서 break 안걸리고 (=연이어서 같은숫자안나오면) 여기로 오게됨
                print('#{} '.format(tc), *arr, sep = '') #연이어서 같은숫자가 없는 arr 배열을 출력하고 중단
                break
            i =0 #arr리스트 다시 처음부터 순회

        #2)같은숫자나올때까지 인덱스 증가시켜서 순회함
        else:
            i+=1
