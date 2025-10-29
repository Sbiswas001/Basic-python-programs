from typing import List

def selectionSort(A: List[int]) -> None:
    # time complexity-- O(n^2)
    # space complexity-- O(1)
    n = len(A)
    for i in range(0, n):
        M = i #Minimum value index
        for j in range(i+1, n):
            if A[j] < A[M]:
                M = j
        A[i], A[M] = A[M], A[i]

#__main__
myArr = [-15,-4,21,5,-3,7,14,10,1,6,-8,2,15,1,-3,34,7,16,81,4,19,-45,8,-12,39]
selectionSort(myArr)
print(myArr)