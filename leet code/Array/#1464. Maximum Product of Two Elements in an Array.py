
#1464. Maximum Product of Two Elements in an Array



nums = [3,4,5,2]
nums2 = [1,5,4,5]
nums3 = [3,7]

#first solution

def maxProduct(nums):
    nums.sort(reverse=True)
    return (nums[0]-1) * (nums[1]-1)

print(maxProduct(nums))
print(maxProduct(nums2))
print(maxProduct(nums3))


#second solution
def maxProduct2(nums):
    max1 = max(nums)
    nums.remove(max1)
    max2 = max(nums)
    return (max1 - 1) * (max2 - 1)


print(maxProduct2(nums))
print(maxProduct2(nums2))
print(maxProduct2(nums3))

