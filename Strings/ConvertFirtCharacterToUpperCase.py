def fun():
    str=input("Enter the sentence = ")
    ans=""
    list=str.split(' ')
    for ch in list: 
        ans=ans+((ch[0].upper()+(ch[1:len(ch)+1]).lower())+" ")
    print("The resultant string is = ",ans)
    
fun()
