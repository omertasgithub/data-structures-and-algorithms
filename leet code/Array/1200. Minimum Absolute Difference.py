#1200. Minimum Absolute Difference

#related topics ->> 
#array


arr = [4,2,1,3]

#first solution        
def minimumAbsDifference(arr):
    arr.sort()
    diff = []
    for i in range(len(arr)):
        if i+1 == len(arr):
            break
        diff.append(arr[i+1]-arr[i])
        
        
    minimum = min(diff)
    
    lst = []
    
    for i in range(len(arr)):
        if i+1==len(arr):
            break
        if minimum == arr[i+1]-arr[i]:
            lst.append([arr[i],arr[i+1]])
    return lst


#second solution
def minimumAbsDifference2(arr):
    arr.sort()
    minimum = []
    for i,j in zip(arr, arr[1:]):
        minimum += [j-i]
    minimum = min(minimum)
    lst = []
    for i,j in zip(arr, arr[1:]):
        if minimum == j-i:
            lst.append([i,j])
    return lst

#third solution
    
def minimumAbsDifference3(arr):
    arr.sort()
    mn = min(b-a for a,b in zip(arr, arr[1:]))
    return [[a,b] for a,b in zip(arr, arr[1:]) if b-a==mn]