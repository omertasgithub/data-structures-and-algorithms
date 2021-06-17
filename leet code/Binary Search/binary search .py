#binary search 
def binary_search(arr, low, high, x):
    if high >= low:
        
        mid = (high + low) // 2
        #if the element present at the middle
        if arr[mid]==x:
            return mid
        #if the element smaller than mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1,x)
        #else the element is in the right
        else:
            return binary_search(arr, mid+1, high,x)
    else:
        return -1
    
arr = [2,3,4,10,40]
print(binary_search(arr,0, len(arr)-1,4))
print(binary_search(arr,0, len(arr)-1,11))

#itertive

def binary_search(arr,x):
    low=0
    high=len(arr)-1
    mid = 0
    
    while low <= high:
        
        mid = (high+low)//2
        
        #if x is greater ignore lef
        if arr[mid] <x:
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            return mid
    return -1

print(binary_search(arr,10))


        