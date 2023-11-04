def fctr(n):
    if n == 1:
        print("پایان")
        return 1
    else:
        result = n * fctr(n - 1)
        return result
#aI