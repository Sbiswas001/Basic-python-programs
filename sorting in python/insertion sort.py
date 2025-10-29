from typing import List

def insertionSort(A: List[int]) -> None:
    # Time complexity-- O(n^2)
    # Space complexity-- O(1)
    n = len(A)
    for i in range(1,n):
        for j in range(i,0,-1):
            if A[j - 1] > A[j]:
                #swap
                A[j - 1], A[j] = A[j], A[j - 1]
            else:
                break

#__main__
myArr = [-15,-4,21,5,-3,7,14,10,1,6,-8,2,15,1,-3,34,7,16,81,4,19,-45,8,-12,39]
insertionSort(myArr)
print(myArr)