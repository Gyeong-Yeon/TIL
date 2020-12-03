arr = [[1,2,3],[4,5,6],[7,8,9]]
print(arr)

rotated = [list(line[::-1]) for line in zip(*arr)]
print(rotated)
