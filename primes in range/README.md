## 🔢 Prime Numbers in a Given Range

**File:** `prime_in_range.py`

### 🧠 About

This Python program prints all prime numbers within a user-defined range.
It uses an optimized check up to the square root of each number to keep it efficient even for larger ranges.

---

### 🧩 Features

* Takes **start** and **end** input from the user.
* Checks each number using a reusable function `is_prime()`.
* Displays all prime numbers in the range (if any).
* Handles invalid input and incorrect ranges gracefully.

---

### ▶️ How to Run

1. Clone or download the repository.
2. Open a terminal or command prompt in the project folder.
3. Run the program:

   ```bash
   python prime_in_range.py
   ```
4. Enter your desired range when prompted.

---

### 💡 Example Output

```
Prime Numbers in a Given Range
Enter starting number: 10
Enter ending number: 30
Prime numbers between 10 and 30 are:
11 13 17 19 23 29
```

---

### ⚙️ Logic Behind It

* A number `n` is prime if it’s divisible only by `1` and `n`.
* The program checks divisibility only up to `√n` for efficiency.
* Non-positive numbers and 1 are excluded automatically.

---

### 🏗️ Next Improvements

* Save results to a file like `primes.txt`.
* Highlight primes using colors (`colorama` module).
* Add a small web version using Flask or Streamlit later.
