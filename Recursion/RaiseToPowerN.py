x=int(input("Enter the base = "))
n=int(input("Enter the exponent = "))
def pow(x,n):
    if n==1:return x
    return x*pow(x,n-1)

print("The resultant number formed is = ")
print(pow(x,n))
