def numbers():
    num1 = float(input("عدد اول را وارد کنید: "))
    num2 = float(input("عدد دوم را وارد کنید: "))

    if num1 > num2:
        print("اولی بزرگتر از دومی است.")
    elif num1 < num2:
        print("اولی کوچکتر از دومی است.")
    else:
        print("اولی با دومی برابر است.")

numbers()