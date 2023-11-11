def pd(string):
    string = string.lower() 
    string = ''.join(char for char in string if char.isalpha())

    return string == string[::-1]

input_string = "Aliazimi"
result = pd(input_string)
print(result)
#aI