arr = list(map(int,input().split()))
arr.sort(reverse=True)

ten = {}
for i in range(len(arr)):
    if arr[i] != 0:
        ten[(arr[i]//10)*10] = 0

for i in range(len(arr)-1):
    ten[(arr[i]//10)*10] += 1

for key in ten.keys():
    print("{} : {} person".format(key, ten[key]))