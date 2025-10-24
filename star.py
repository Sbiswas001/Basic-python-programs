n=int(input("Enter : "))

for i in range(n):
    for k in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

for a in range(n):
    for c in range(a):
        print(" ",end="")
    for b in range(2*(n-a)-1):
        print("*",end="")
    print()
