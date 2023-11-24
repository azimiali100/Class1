def tool(str1, str2):
    if len(str1) > len(str2):
        return "رشته 1 بلندتر است."
    elif len(str1) < len(str2):
        return "رشته 2 بلندتر است."
    else:
        return "برابر"

print(tool('hello', 'world'))