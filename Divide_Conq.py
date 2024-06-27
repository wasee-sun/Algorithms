
#? Linear vs divide and conquer

# def max_num(arr): #linear search
#     maxi = 0
#     if len(arr) == 1:
#         return arr[0]
#     for ele in arr:
#         if ele > maxi:
#             maxi = ele 
                
#     return maxi

def max_num(arr): #* Divide and Conquer
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left = max_num(left_arr)
    right = max_num(right_arr)
    
    return max(left, right)


if __name__ == "__main__":
    arr = [15, 24, 89, 54, 34] # 56, 46, 21, 90, 83
    print(max_num(arr))
    
            