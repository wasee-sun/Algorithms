def mergesort(arr1, arr2):
    if len(arr1) == 1: # if only one item is left return it
        return arr1, arr2
    
    k_arr1 = [] # sorted array
    k_arr2 = [] # sorted array
    mid = len(arr1) // 2 #midpoint
    left_arr1 = arr1[:mid] # left array
    right_arr1 = arr1[mid:] # right array
    left_arr2 = arr2[:mid] # left array
    right_arr2 = arr2[mid:] # right array
    
    left_arr1, left_arr2 = mergesort(left_arr1, left_arr2) # recursion on left array
    right_arr1, right_arr2 = mergesort(right_arr1, right_arr2) # recursion on right array
    
    i = 0 # index of left array
    j = 0 # index of right array
    
    while i < len(left_arr1) and j < len(right_arr1): # looping until both left and right index is in bound
        if left_arr1[i] / left_arr2[i] > right_arr1[j] / right_arr2[j]: # if left item is less than right item
            k_arr1.append(left_arr1[i])
            k_arr2.append(left_arr2[i])
            i += 1 # next item
        else: # if right item is less than left item
            k_arr1.append(right_arr1[j])
            k_arr2.append(right_arr2[j])
            j += 1 # next itme
    
    while i < len(left_arr1): # if item left in left array
        k_arr1.append(left_arr1[i])
        k_arr2.append(left_arr2[i])
        i += 1
        
    
    while j < len(right_arr1): # if item left in right array
        k_arr1.append(right_arr1[j])
        k_arr2.append(right_arr2[j])
        j += 1
        
    return k_arr1, k_arr2 # return the sorted array


def frac_knapsack(v, w, k):
    v, w = mergesort(v, w)
    total_w = 0
    total_v = 0
    i = 0
    while total_w != k:
        if i == len(v):
            break
        if total_w + w[i] < k:
            total_w += w[i]
            total_v += v[i]
            i += 1
        else:
            rem_cap = k - total_w
            frac_cap = rem_cap / w[i]
            total_w += rem_cap
            total_v += v[i] * frac_cap
            i += 1
            
    return total_v
            


if __name__ == '__main__':
    val = [20, 30, 15, 25, 10]
    weights = [6, 13, 5, 10, 3]
    k = 20
    print(frac_knapsack(val, weights, k))