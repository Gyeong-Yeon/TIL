S, E = map(int,input().split())

if S > E:
    S, E = E, S # SWAP

for i in range(S, E+1):
    print(i, end=" ")