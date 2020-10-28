def fill():
    num = ord('A') # 65
    for i in range(N): # 행
        j = i
        k = N-1
        while j < N:
            arr[j][k] = chr(num)
            num += 1
            if chr(num) > 'Z':
                num = ord('A')
            k -= 1
            j += 1

def printAll():
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()

N = int(input())
arr = [[' ']*N for _ in range(N)]
fill()
printAll()