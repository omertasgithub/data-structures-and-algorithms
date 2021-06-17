#704. Binary Search
#related topics
#binary search

#brute force

nums1 = [-1,0,3,5,9,12]
target1 = 9
nums2 = [-1,0,3,5,9,12]
target2 = 2

#first solution
def search(nums,target):
    if target not in nums:
        return -1
    else:
        return nums.index(target)
    
print(search(nums1, target1))
print(search(nums2, target2))

#iteration
def search(nums, target):
    low,high = 0, len(nums)-1
    
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] <target:
            low = mid+1
        else:
            high = mid-1
    else:
        return -1

print(search(nums1, target1))
print(search(nums2, target2))