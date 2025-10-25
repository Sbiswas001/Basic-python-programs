import random

def main():
    number = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("🎉 Congratulations! You guessed the number correctly.")
    else:
        print(f"❌ Sorry, the correct number was {number}. Better luck next time!")

if __name__ == "__main__":
    main()
