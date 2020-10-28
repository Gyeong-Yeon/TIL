def fill():
    num = ord('A') # 65
    for i in range(n-1, -1, -1): # 행
        for j in range(n-1, -1, -1): # 열
            arr[j][i] = chr(num)
            num += 1
            if chr(num) > 'Z':
                num = ord('A')

def printAll():
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()

n = int(input())
arr = [[' '] * n for _ in range(n)]
fill()
printAll()