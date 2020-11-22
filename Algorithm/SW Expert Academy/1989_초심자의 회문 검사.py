import sys
sys.stdin = open('input_초심자의 회문 검사.txt')

T = int(input())

for tc in range(1, T+1):
    arr = input()
    for i in range(len(arr)):
        if arr == arr[::-1]:
            result = 1
        else:
            result = 0

    print("#{} {}".format(tc, result))