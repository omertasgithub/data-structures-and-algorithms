#1413. Minimum Value to Get Positive Step by Step Sum
#related topics
#array

nums = [-3,2,-3,4,2]
nums2 = [1,2]
nums3 = [1,-2,-3]

#first solution
def minStartValue(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lst = []
    for i in range(len(nums)):
        lst+=[sum(nums[:(i+1)])]
    x = min(lst)
    if x>0:
        return 1
    else:
        return  abs(x)+1
    
def minStartValue(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lst = []
    for i in range(len(nums)):
        lst+=[sum(nums[:(i+1)])]
    x = min(lst)
    if x>0:
        return 1
    else:
        return  abs(x)+1


