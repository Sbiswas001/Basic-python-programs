def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    if num == 2:
        return True   # 2 is prime
    if num % 2 == 0:
        return False  # even numbers greater than 2 are not prime

    # Check divisibility from 3 to √num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

