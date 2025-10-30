from typing import List

def quickSort(A: List[int]) -> List[int]:
    n = len(A)
    if n <= 1:
        # base case
        return A
    
    p = A[-1]
    L = [x for x in A[:-1] if x <= p]
    R = [x for x in A[:-1] if x > p]
    
    # recursion
    L = quickSort(L)
    R = quickSort(R)

    # concatination
    return L + [p] + R

#__main__
myArr = [-15,-4,21,5,-3,7,14,10,1,6,-8,2,15,1,-3,34,7,16,81,4,19,-45,8,-12,39]
myArr = quickSort(myArr)
print(myArr)