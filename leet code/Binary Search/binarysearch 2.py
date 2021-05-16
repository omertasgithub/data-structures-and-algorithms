
#binary search
#best case O(1) worst case O(logn)

#recursive
def binary_search(arr, low, high, x):
    
    #check base
    if high >= low:
        mid = (high + low) // 2
        
        #if element is present at the middle itself
        if arr[mid] == x:
            return mid
        #if element is smaller than mid, then it can only
        #be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1,x)
        #Else element can be ony be present in the right subarray
        
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1
    
arr = [2,3,4,10,40]
high = len(arr)-1
low = 0   
x=10
print(binary_search(arr, low, high,x))


#iterative binary search
def binary_search2(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        
        #If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        
        #if x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
            
        #means x is present at mid
        else:
            return mid
    
    #if we reac here, then the element was not present
        
    return -1

    
print(binary_search2(arr,10))

        