user = "alihaSANI4@$#+"

upper = ""
lower = ""
put = ""

for char in user:
    if char.isupper():
        upper += char
    elif char.islower():
        lower += char
    else:
        put += char

print("حروف بزرگ:", upper)
print("حروف کوچک:", lower)
print("علائم:", put)