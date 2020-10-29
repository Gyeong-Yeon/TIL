S, E = map(str,input().split())

score = {'1': 85.6,
'2': 79.5,
'3': 83.1,
'4': 80.0,
'5': 78.2,
'6': 75.0
}

sum = score[S] + score[E]
print("%0.1f" % sum)