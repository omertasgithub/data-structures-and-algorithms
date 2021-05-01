#561. Array Partition I
#related topics
#array



nums = [1,4,3,2]
nums2 = [6,2,6,5,1,2]

#first solution
def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    
    for i in range(0, len(nums),2):
        max_sum+=nums[i]
    return max_sum

print(arrayPairSum(nums))
print(arrayPairSum(nums2))


#Second solution
def arrayPairSum2(nums):
    return sum(sorted(nums)[::2])

print(arrayPairSum2(nums))
print(arrayPairSum2(nums2))