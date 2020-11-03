W = float(input())

if W <= 50.80:
    print("Flyweight")
elif 50.80 < W <= 61.23:
    print("Lightweight")
elif 61.23 < W <= 72.57:
    print("Middleweight")
elif 72.57 < W <= 88.45:
    print("Cruiserweight")
else:
    print("Heavyweight")

