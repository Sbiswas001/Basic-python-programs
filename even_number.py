# Take user input and convert it into an integer
# input() reads data as a string, so we use int() to convert it to an integer
even = int(input("Enter a number: "))

# Loop through all numbers starting from 2 up to (but not including) the entered number
for i in range(2, even):
    
    # Check if the current number is even using the modulus operator (%)
    # If remainder when divided by 2 is 0, then the number is even
    if i % 2 == 0:
        
        # Print the even number using an f-string for formatted output
        print(f"{i} is an even number")
