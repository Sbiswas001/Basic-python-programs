import random as r
import time 
def Toss():
    result=r.choice(["Heads","Tails"])
    return result
print("🪙 Coin Toss Simulator 🪙")
while True:
    user_input = input("Press Enter to toss the coin or type 'exit' to quit: ").lower()

    if user_input == "exit":
        print("Thanks for playing! 👋")
        break
    else:
        print("\nTossing the coin", end="", flush=True)
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        time.sleep(0.5)


        result = Toss()
        print(f"\nResult: {result}")
        print("-" * 30)