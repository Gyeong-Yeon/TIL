def fill2():
    num = 1
    for i in range(n): # 행
        if i % 2 == 0: # 짝수행
            for j in range(m): # 열
                arr[i][j] = num
                num += 1
        else: # 홀수행
            for j in range(m-1,-1,-1): # 열
                arr[i][j] = num
                num += 1

def printAll():
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=" ")
        print()

n, m = map(int,input().split())
arr = [[0] * m for _ in range(n)]
fill2()
printAll()