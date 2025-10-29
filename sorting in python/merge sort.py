from typing import List

def mergeSort(A: List[int]) -> List[int]:
    # Time complexity-- O(nlogn)
    # Space complexity-- O(n)
    n = len(A)
    if n <= 1:
        return A
    m = n // 2
    L = mergeSort(A[:m])
    R = mergeSort(A[m:])
    l, r = 0, 0
    sortedA = []
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            sortedA.append(L[l])
            l += 1
        else:
            sortedA.append(R[r])
            r += 1
    # Add remaining elements
    while l < len(L):
        sortedA.append(L[l])
        l += 1
    while r < len(R):
        sortedA.append(R[r])
        r += 1
    return sortedA

#__main__
myArr = [-15,-4,21,5,-3,7,14,10,1,6,-8,2,15,1,-3,34,7,16,81,4,19,-45,8,-12,39]
print(mergeSort(myArr))