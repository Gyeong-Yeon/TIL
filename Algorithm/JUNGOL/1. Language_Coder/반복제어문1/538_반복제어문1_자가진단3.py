while True:
    print(f'number? ', end="")
    N = int(input())
    if N > 0:
        print("positive integer")
    elif N < 0:
        print("negative number")
    else:
        break

