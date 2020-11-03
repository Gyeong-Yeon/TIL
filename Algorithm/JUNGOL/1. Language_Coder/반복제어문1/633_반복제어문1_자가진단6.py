print(f'1. Korea')
print(f'2. USA')
print(f'3. Japan')
print(f'4. China')
print(f'number?', end=" ")
N = int(input())
print()
capital = [' ', 'Seoul', 'Washington', 'Tokyo', 'Beijing']
if  0 < N < len(capital):
    print(capital[N])
else:
    print('none')
