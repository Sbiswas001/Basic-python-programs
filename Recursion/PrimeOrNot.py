def isPrime(n, i = 2):
    if (n <= 2): return True if(n == 2) else False
    if (n % i == 0): return False
    if (i * i > n): return True
    return isPrime(n, i + 1)

num=int(input("Enter the number = "))
if(isPrime(num)):print("Prime Number")
else : print("Not a Prime Number")
