
#852. Peak Index in a Mountain Array
#binary search
arr1 = [0,1,0]
arr2 = [0,2,1,0]
arr5 = [24,69,100,99,79,78,67,36,26,19]

#first solution
def peakIndexInMountainArray(arr):
        
        dic = {}
        for i,n in enumerate(arr):
            dic[i]=n
        dic_sort = sorted(dic.items(),key=lambda x:-x[1])
        return dic_sort[0][0]
    
print(peakIndexInMountainArray(arr1))
print(peakIndexInMountainArray(arr2))
print(peakIndexInMountainArray(arr5))

#second solution
def peakIndexInMountainArray(arr):
    maximum = 0
    for i,n in enumerate(arr):
        maximum = max(maximum,n)
    return arr.index(maximum)
print(peakIndexInMountainArray(arr1))
print(peakIndexInMountainArray(arr2))
print(peakIndexInMountainArray(arr5))

#really
def peakIndexInMountainArray(arr):
    
    return arr.index(max(arr))
print(peakIndexInMountainArray(arr1))
print(peakIndexInMountainArray(arr2))
print(peakIndexInMountainArray(arr5))