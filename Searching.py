#Algorithms
#! Searching algorithms
from Sorting import mergesort

def linear_search(arr, ele):
    for i in range(len(arr)):
        if ele == arr[i]:
            return True
        
    return False

def binary_search(arr, ele):
    if len(arr) == 0:
        return False
    
    mid = len(arr) // 2
    if arr[mid] == ele:
        return True
    elif ele < arr[mid]:
        return binary_search(arr[:mid], ele)
    elif ele > arr[mid]:
        return binary_search(arr[mid+1:], ele)

def ternary_search(arr, ele):
    if len(arr) == 0:
        return False
    
    one_third = len(arr) // 3
    two_third = one_third * 2
    
    if arr[one_third] == ele or arr[two_third] == ele:
        return True
    
    if ele < arr[one_third]:
        return ternary_search(arr[:one_third], ele)
    elif ele > arr[one_third] and ele < arr[two_third]:
        return ternary_search(arr[one_third + 1 : two_third], ele)
    else:
        return ternary_search(arr[two_third + 1:], ele)

def quadratic_search(arr, ele):
    if len(arr) == 0:
        return False
    
    mid = len(arr) // 2
    first_mid = mid // 2
    second_mid = mid // 2 + mid
    
    if arr[mid] == ele or arr[first_mid] == ele or arr[second_mid] == ele:
        return True
    
    if ele < arr[mid]:
        if ele < arr[first_mid]:
            return quadratic_search(arr[:first_mid], ele)
        else:
            return quadratic_search(arr[first_mid + 1 : mid], ele)
    else:
        if ele < arr[second_mid]:
            return quadratic_search(arr[mid + 1: second_mid], ele)
        else:
            return quadratic_search(arr[second_mid + 1:], ele)

if __name__ == '__main__':
    arr = [99, 27, 7, 34, 230, 967, 1568, 78, 83, 48, 5, 120]
    sorted_arr = mergesort(arr)
    print(arr)
    print(sorted_arr)
    print(linear_search(arr, 967))
    print(binary_search(sorted_arr, 967))
    print(ternary_search(sorted_arr, 967))
    print(quadratic_search(sorted_arr, 967))
    