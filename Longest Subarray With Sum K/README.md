**Problem Statement:**

You are given an array 'a' of size 'n' and an integer 'k'.
Find the length of the longest subarray of 'a' whose sum is equal to 'k'.

---

**Example :**

Input: ‘n’ = 7, ‘k’ = 3  
‘a’ = [1, 2, 3, 1, 1, 1, 1]

Output: 3

Explanation: Subarrays whose sum = ‘3’ are:
[1, 2], [3], [1, 1, 1], and [1, 1, 1]

Here, the length of the longest subarray is **3**, which is our final answer.

---

### 📝 Detailed Explanation

**Sample Input 1 :**
```text
7 3
1 2 3 1 1 1 1
```

**Sample Output 1 :**
```text
3
```

Explanation:  
Subarrays whose sum = ‘3’ are:
[1, 2], [3], [1, 1, 1], [1, 1, 1]  
Length of the longest subarray = **3**

---

**Sample Input 2 :**
```text
4 2
1 2 1 3
```

**Sample Output 2 :**
```text
1
```

---

**Sample Input 3 :**
```text
5 2
2 2 4 1 2
```

**Sample Output 3 :**
```text
1
```

---

### ⏱️ Expected Time Complexity
```
O(n)
```

---

### ✅ Constraints
```
1 <= n <= 5 * 10^6
1 <= k <= 10^18
0 <= a[i] <= 10^9
Time Limit: 1 second
```
## ---------------------------------------------------------------------

## Solution Approach

### Concept Used — Sliding Window (Two Pointers)

This problem is solved using the **Sliding Window** approach, which is efficient for arrays containing only **positive integers**.

We maintain two pointers, `l` (left) and `r` (right), representing the current window of elements.  
We also keep a variable `sum` that stores the sum of elements within the window.

### Steps

1. Initialize `l = 0`, `sum = 0`, and `ans = 0`.
2. Iterate with `r` from `0` to `n - 1`:
   - Add `a[r]` to `sum`.
   - While `sum > k`, move `l` forward (shrink the window) and subtract `a[l]` from `sum`.
   - If `sum == k`, update `ans = max(ans, r - l + 1)`.
3. Continue until all elements are processed.
4. Return the value of `ans` as the length of the longest subarray with sum equal to `k`.

### Why Sliding Window Works

The **sliding window** technique works efficiently here because all elements are **non-negative**.  
- When the sum exceeds `k`, we can safely shrink the window from the left to reduce the sum.  
- When the sum is less than or equal to `k`, we expand the window to the right.

This ensures each element is added and removed at most once.

### Time and Space Complexity

- **Time Complexity:** `O(n)` — each element is processed at most twice (once added, once removed).  
- **Space Complexity:** `O(1)` — only a few extra variables are used.

### Example

**Input:**

n = 5, k = 5
arr = [1, 2, 1, 1, 1]


**Process:**
- Window `[1, 2, 1, 1]` → sum = 5 → length = 4

**Output:**

4
