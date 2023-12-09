dic= {'ali': 31, 'reza': 25, 'maryam': 28}

key = 'ali'
b = None

for i in dic:
    if i == key:
        b = dic[key]
        break

print(b)