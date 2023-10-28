def calculator():
    print("سلام! به ماشین حساب خوش آمدید.")
    print("لطفاً دو عدد و عملگر را وارد کنید.")
    
    num1 = float(input("عدد اول: "))
    operator = input("عملگر (+, -, *, /): ")
    num2 = float(input("عدد دوم: "))
    
    result = 0
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("خطا! تقسیم بر صفر ممنوع است.")
            return
    
    print("نتیجه: ", result)
    
calculator()