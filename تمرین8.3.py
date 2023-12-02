z = '@Ab#cdf'
Up = []
Low = []
Symb = []

for i in z:
    if i.isupper():
        Up.append(i)
    elif i.islower():
        Low.append(i)
    else:
        Symb.append(i)

print(Up)
print(Low)
print(Symb)