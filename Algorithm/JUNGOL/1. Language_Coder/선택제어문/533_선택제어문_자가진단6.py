sex, age = map(str,input().split())

if sex == 'M':
    if int(age) >= 18:
        result = 'MAN'
    else:
        result = 'BOY'
else: # sex == 'F'
    if int(age) >= 18:
        result = 'WOMAN'
    else:
        result = 'GIRL'

print(result)
