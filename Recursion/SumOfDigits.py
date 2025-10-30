num=int(input("Enter the number = "))
def sum(num):
    if num==0:return 0
    else:
        dig=num%10
        return dig+sum(num//10)

print("The sum of digits of the number using recurrsion is = ",sum(num))
    
