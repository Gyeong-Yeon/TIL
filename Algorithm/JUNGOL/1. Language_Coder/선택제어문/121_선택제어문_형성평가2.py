N = int(input())

if N == 0:
    result = "zero"
elif N > 0:
    result = "plus"
else: # N < 0
    result = "minus"

print(result)