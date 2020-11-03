print(f'Number? ', end="")
N = int(input())

if N == 1:
    animal = 'dog'
elif N == 2:
    animal = 'cat'
elif N == 3:
    animal = 'chick'
else:
    animal = "I don't know."

print(animal)