#976. Largest Perimeter Triangle
#related topics
#math, sort

nums = [2,1,2]
nums2 = [1,2,1]
nums3 = [3,2,3,4]
nums4 = [3,6,2,3]
#solution 1
def largestPerimeter(nums):
    nums.sort(reverse=True)
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return sum(nums[i:i+3])
            break
            
    return 0
    
print(largestPerimeter(nums))
print(largestPerimeter(nums2))
print(largestPerimeter(nums3))
print(largestPerimeter(nums4))


#solution 2
def largestPerimeter(self, A):
  A.sort()
  return ([0] + [a + b + c for a, b, c in zip(A, A[1:], A[2:]) if c < a + b])[-1]