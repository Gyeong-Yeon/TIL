def fill():
    num = 1
    for i in range(n):
        for j in range(n):
            arr[j][i] = num
            num += 1

def printAll():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()

n = int(input())
arr = [[0] * n for _ in range(n)]
fill()
printAll()