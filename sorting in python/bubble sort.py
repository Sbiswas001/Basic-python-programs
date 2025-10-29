from typing import List

def bubbleSort(A: List[int]) -> None:
    # Time complexity-- O(n^2)
    # Space complexity-- O(1), in-place swapping
    n = len(A)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if (A[i-1] > A[i]):
                #swap
                A[i - 1], A[i] = A[i], A[i - 1]
                flag = True

#__main__
myArr = [-15,-4,21,5,-3,7,14,10,1,6,-8,2,15,1,-3,34,7,16,81,4,19,-45,8,-12,39]
bubbleSort(myArr)
print(myArr)
