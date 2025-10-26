def replace(str):
    if not str: return str
    
    result =str[0]
    prev_char =str[0]
    
    for char in str[1:]:
        if char == prev_char: result += '*'  
        else: result += char  
        prev_char = char  
    return result

str = input("Enter the string = ")
rstr = replace(str)
print("The modified string is = ",rstr)

