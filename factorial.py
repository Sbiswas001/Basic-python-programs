"""
Factorial Program
This program calculates the factorial of a given number.
Factorial of n (n!) = n * (n-1) * (n-2) * ... * 1
"""


def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    # Example usage
    print("Factorial Calculator")
    print("=" * 40)
    
    try:
        num = int(input("Enter a non-negative integer: "))
        
        # Calculate using iterative method
        result_iterative = factorial(num)
        print(f"\nFactorial of {num} (iterative): {result_iterative}")
        
        # Calculate using recursive method
        result_recursive = factorial_recursive(num)
        print(f"Factorial of {num} (recursive): {result_recursive}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
