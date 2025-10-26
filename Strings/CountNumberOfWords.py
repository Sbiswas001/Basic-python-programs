def fun():
    str=input("Enter the sentence = ")
    count=0
    list=str.split(' ')
    for ch in list:count=count+1
    print("The number of words in the sentence is = ",count)
    
fun()
