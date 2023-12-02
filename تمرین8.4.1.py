a = [1, 8, 7, 'amir', True, 4.1]

for i in range(len(a)-1, -1, -1):
    del a[i]

print(a)