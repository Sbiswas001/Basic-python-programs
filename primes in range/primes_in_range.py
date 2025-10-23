def isprime(n): #for checking each number prime or not 
    if n<=1:
        return False
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c<=2:
        return True
    else:
        return False
def primesinrange(start,end):
    primes = []
    for num in range(start, end + 1):
        if isprime(num):
            primes.append(num)
    return primes
if __name__ == "__main__":
    print("Prime Numbers in a Given Range")
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("⚠️ Start should be less than or equal to end.")
        else:
            primes = primesinrange(start, end)
            if primes:
                print("Prime numbers between", start, "and", end, "are:")
                print(*primes)
            else:
                print("No prime numbers found in this range.")
    except ValueError:
        print("❌ Please enter valid integers.")                        