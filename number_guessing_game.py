import random

def play_number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check if guess is correct
            if guess == secret_number:
                print(f"\nCongratulations! You've guessed the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            # Show remaining attempts
            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number!")
            continue

    print(f"\nGame Over! The number was {secret_number}.")

if __name__ == "__main__":
    play_number_guessing_game()