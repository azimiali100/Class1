dict = {
    "apple": "سیب",
    "banana": "موز",
    "car": "ماشین",
    "house": "خانه",
    "book": "کتاب"
}

while True:
    i = input("کلمه انگلیسی را وارد کنید (برای خروج عبارتی مثل 'exit' را وارد کنید): ")

    if i == "exit":
        break

    if i in dict:
        trans = dict[i]
        print("معادل فارسی کلمه", i, ":", trans)
    else:
        print("معادل فارسی برای کلمه", i, "یافت نشد.")