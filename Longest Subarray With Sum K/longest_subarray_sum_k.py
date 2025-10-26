def longestSubarrayWithSumK(a, k, n):
    l = 0
    r = 0
    total = 0
    ans = 0

    while r < n:
        total += a[r]

        while l <= r and total > k:
            total -= a[l]
            l += 1

        if total == k:
            ans = max(ans, r - l + 1)

        r += 1

    return ans


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(longestSubarrayWithSumK(arr, k, n))
