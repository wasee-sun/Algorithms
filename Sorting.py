#Algorithms
#! Sorting algorithms

def bubblesort(arr):
    """
    Bubbling up the lowest value to the top
    by comparing with each other
    
    Time Complextity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr)): # each item
        for j in range(len(arr) - 1): #compared with other items
            # if arr[i] < arr[j]: # for decending order
            if arr[j] > arr[j + 1]: # if we get a lower value
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # switching
    
    return arr

def selectionsort(arr):
    """
    Find the minimum item
    Comparing it each item to find the minimum
    Selecting the minimum value and swapping indexes
    
    Time Complextity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr)): # each item
        min_idx = i # index of item
        for j in range(i + 1, len(arr)): # comparing right side items
            # if arr[j] > arr[i]: # for decending order
            if arr[j] < arr[min_idx]: # if we get a lower value
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx] # switching
        
    return arr

def insertionsort(arr):
    """
    Find the anchor item
    Comparing it with the left side (sorted array)
    Inserting the anchor value to its position
    
    Time Complextity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr)): # each item
        anchor = arr[i] # index of item
        j = i - 1 # previous item index
        while j >= 0 and anchor < arr[j]: # if j item is less than i
            if anchor < arr[j]: # if j item is greater than i item
                arr[j + 1] = arr[j] # replacing next item with j item
            j -= 1 # going to the previous item
        arr[j + 1] = anchor # putting anchor in it's position
        
    return arr

def mergesort(arr):
    """
    Finding the mid item and spliting the array into two
    creating a left and right array
    recusion until there is only one item left
    comparing items of left and right array and creating a sorted array
    
    Time Complextity: O(nlog(n))
    Space Complexity: O(n)
    """
    if len(arr) == 1: # if only one item is left return it
        return arr
    
    mid = len(arr) // 2 #midpoint
    left_arr = arr[:mid] # left array
    right_arr = arr[mid:] # right array
    
    left_arr = mergesort(left_arr) # recursion on left array
    right_arr = mergesort(right_arr) # recursion on right array
    
    i = 0 # index of left array
    j = 0 # index of right array
    k_arr = [] # sorted array
    
    while i < len(left_arr) and j < len(right_arr): # looping until both left and right index is in bound
        if left_arr[i] < right_arr[j]: # if left item is less than right item
            k_arr.append(left_arr[i])
            i += 1 # next item
        else: # if right item is less than left item
            k_arr.append(right_arr[j])
            j += 1 # next itme
    
    while i < len(left_arr): # if item left in left array
        k_arr.append(left_arr[i])
        i += 1
        
    
    while j < len(right_arr): # if item left in right array
        k_arr.append(right_arr[j])
        j += 1
        
    return k_arr # return the sorted array

def quicksort_hoare(arr): #* Hoare Partition
    """
    Pivot is the first item
    taking first item as left idx and last item as right idx
    if right item is less than pivot and left item is greater than pivot
    switch the items
    loop ends if end idx crosses start idx
    switches pivot with end_idx item
    divides array into two arrays excluding pivot
    recursion on the left and right array
    
    Time Complextity: O(nlog(n)) (worst case O(n^2))
    Space Complexity: O(log(n))
    """
    if len(arr) <= 1: # if no item of 1 item left return arr
        return arr
    
    pivot = arr[0] # pivot item
    start_idx = 1 # starting idx
    end_idx = len(arr) - 1 # ending idx
    
    while end_idx >= start_idx: # looping until end idx crosses start idx
        if arr[start_idx] <= pivot: # if start idx item is less than pivot
            start_idx += 1
            continue # go to next item and continue
            
        if arr[end_idx] > pivot: # if end idx item is greater than pivot
            end_idx -= 1
            continue # go to next item and continue
        
        if arr[end_idx] < pivot: # if endidx item is lesser than pivot
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx] # switch the end item with start item and vice versa
     
    arr[0], arr[end_idx] = arr[end_idx], arr[0] # switch pivot with end item and vice versa
    
    left_arr = arr[:end_idx] # left array except pivot
    right_arr = arr[end_idx + 1:] # right array except pivot
    
    left_arr = quicksort_hoare(left_arr) # recursion on the left array
    right_arr = quicksort_hoare(right_arr) # recursion on the right array
    
    return left_arr + [pivot] + right_arr # return left + pivot + right arrays 

def quicksort_lomuto(arr): #* Lomuto Partition
    """
    Pivot is the first item
    taking first item as left idx and last item as right idx
    if right item is less than pivot and left item is greater than pivot
    switch the items
    loop ends if end idx crosses start idx
    switches pivot with end_idx item
    divides array into two arrays excluding pivot
    recursion on the left and right array
    
    Time Complextity: O(nlog(n)) (worst case O(n^2))
    Space Complexity: O(log(n))
    """
    if len(arr) <= 1: # if no item of 1 item left return arr
        return arr
    
    pivot = arr[-1] # pivot item
    p_idx = 0 # p_index
    i = p_idx # i index
    
    while i != len(arr) - 1: # looping until end idx crosses start idx
        if arr[p_idx] < pivot: # if p idx item is less than pivot
            p_idx += 1
            if i < p_idx: # changing i value only if it is less than p_idx
                i += 1
            continue # go to next item and continue
            
        if arr[i] >= pivot: # if end i idx is greater than pivot
            i += 1
            continue # go to next item and continue
        
        if arr[i] < pivot: # if i idx item is lesser than pivot
            arr[p_idx], arr[i] = arr[i], arr[p_idx] # switch the i_idx with p_idx and vice versa
     
    arr[-1], arr[p_idx] = arr[p_idx], arr[-1] # switch pivot with p_idx and vice versa
    
    left_arr = arr[:p_idx] # left array except pivot
    right_arr = arr[p_idx + 1:] # right array except pivot
    
    left_arr = quicksort_lomuto(left_arr) # recursion on the left array
    right_arr = quicksort_lomuto(right_arr) # recursion on the right array
    
    return left_arr + [pivot] + right_arr # return left + pivot + right arrays 
            
def shell_sort(arr):
    return _shell_sort(arr, len(arr)// 2)

def _shell_sort(arr, n):
    if n == 0:
        return arr
    
    for i in range(n, len(arr)):
        if arr[i] < arr[i - n]:
            arr[i], arr[i - n] = arr[i - n], arr[i]
       
    return _shell_sort(arr, n // 2)
 
def max_heapify(heap, idx):
    left_idx = (2 * idx) + 1
    right_idx = (2 * idx) + 2
    min_idx = None
    
    if left_idx >= len(heap):
        return heap
    
    if right_idx >= len(heap):
        min_idx = left_idx
    else:
        if heap[left_idx] > heap[right_idx]:
            min_idx = left_idx
        else:
            min_idx = right_idx
            
    if heap[idx] < heap[min_idx]:
        heap[min_idx], heap[idx] = heap[idx], heap[min_idx]
    return max_heapify(heap, min_idx)  
        
def heapsort(arr):
    for i in range(len(arr) - 1, -1, -1):
        arr = max_heapify(arr, i)
        
    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        arr = max_heapify(arr[:i], 0) + arr[i:]
    
    return arr

#* Rest sorting functions are only for numbers
def counting_sort(arr):
    max_ele = max(arr)
    k_arr = [0] * (max_ele + 1)
    for ele in arr:
        k_arr[ele] += 1
    for i in range(1, len(k_arr)):
        k_arr[i] += k_arr[i - 1]
    
    sorted_arr = [0] * len(arr)
    for i in range(len(sorted_arr) - 1, -1, -1):
        k_arr[arr[i]] -= 1
        sorted_arr[k_arr[arr[i]]] = arr[i]
        
    return sorted_arr

def count_places(num):
    if num == 0:
        return 0
    num = num // 10
    return count_places(num) + 1

def find_idx(ele, count):
    ele = ele % (10 ** (count + 1))
    ele = ele // (10 ** count)
    return ele
        
def radix_sort(arr):
    max_ele = max(arr)
    d = count_places(max_ele)
    
    return _radix_sort(arr, d, 0)

def _radix_sort(org_arr, d, count):
    if d == count:
        return org_arr
    
    k_arr = [0] * 10
    for i in range(len(org_arr)):
        idx = find_idx(org_arr[i], count)
        k_arr[idx] += 1
        
    for i in range(1, len(k_arr)):
        k_arr[i] += k_arr[i - 1]
        
    sorted_arr = [0] * len(org_arr)
    for i in range(len(sorted_arr) - 1, -1, -1):
        idx = find_idx(org_arr[i], count)
        k_arr[idx] -= 1
        sorted_arr[k_arr[idx]] = org_arr[i]
    
    print(sorted_arr)
    return _radix_sort(sorted_arr, d, count + 1)

def bucket_sort(arr):
    max_ele = max(arr)
    count = count_places(max_ele)
    return _bucket_sort(arr, count, 0)

def _bucket_sort(arr, count, c_idx):
    if c_idx == count:
        return arr
    k_arr = [None] * 10
    for i in range(len(arr)):
        idx = find_idx(arr[i], c_idx)
        if k_arr[idx] is None:
            k_arr[idx] = [arr[i]]
        else:
            k_arr[idx].append(arr[i])
    sorted_arr = [0] * len(arr)
    n = 0
    for i in range(len(k_arr)):
        if k_arr[i] is not None:
            k_arr[i] = insertionsort(k_arr[i])
            for j in range(len(k_arr[i])):
                sorted_arr[n] = k_arr[i][j]
                n += 1
                
    return _bucket_sort(sorted_arr, count, c_idx + 1)

  
if __name__ == "__main__":      
    arr = [9, 7, 3, 3, 2, 5, 5, 7, 7, 9] # for counting sort
    arr = [99, 27, 7, 34, 230, 967, 1568, 78, 83, 48, 5, 120]
    arr = [89, 53, 150, 36, 633, 233]
    arr = [8, 9, 2, 5, 20, 7, 1]

    # print(bubblesort(arr))
    # print(selectionsort(arr))
    # print(insertionsort(arr))
    # print(mergesort(arr))
    print(quicksort_hoare(arr))
    # print(quicksort_lomuto(arr))
    # print(shell_sort(arr))
    # print(heapsort(arr))
    # print(counting_sort(arr))
    # print(radix_sort(arr))
    # print(bucket_sort(arr))