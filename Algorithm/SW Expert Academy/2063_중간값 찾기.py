N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
mid = numbers[N//2]
print(mid)