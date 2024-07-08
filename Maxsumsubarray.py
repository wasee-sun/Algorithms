# Maxsumsubarray

def max_sumsubarray(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr)//2
    lss = max_sumsubarray(arr[:mid]) #6
    rss = max_sumsubarray(arr[mid:]) #6
    
    css_left = None
    css_right = None
    css_left_current = None
    css_right_current = None
    i = mid - 1
    j = mid
    
    while i >= 0:
        if css_left is None:
            css_left = arr[i]
            css_left_current = arr[i]
            i -= 1
            continue
        css_left_current += arr[i]
        css_left = max(css_left, css_left_current)
        i -= 1
    while j < len(arr):
        if css_right is None:
            css_right = arr[j]
            css_right_current = arr[j]
            j += 1
            continue
        css_right_current += arr[j]
        css_right = max(css_right, css_right_current)
        j += 1
        
    css = css_left + css_right
    
    return max(lss, css, rss)

if __name__ == '__main__':
    array = [-2, -5, 6, -2, -3, 1, 5, -6]
    array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_sumsubarray(array))
    
    
    
    