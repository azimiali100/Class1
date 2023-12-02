a = [1, 8, 7, 'amir', True, 4.1]

lst = a[:]
for i in lst:
    a.remove(i)

print(a)