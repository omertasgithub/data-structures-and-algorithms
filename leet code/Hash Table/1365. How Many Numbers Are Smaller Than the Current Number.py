#1365. How Many Numbers Are Smaller Than the Current Number
#realted topics
#array, hash table

nums = [8,1,2,2,3]
nums2 = [6,5,4,8]
nums3 = [7,7,7,7]
    
#first solution
def smallerNumbersThanCurrent(nums):
    res = []
    for i in nums:
        r=0
        for j in nums:
            if j<i:
                r+=1
        res.append(r)
    return res


print(smallerNumbersThanCurrent(nums))
print(smallerNumbersThanCurrent(nums2))
print(smallerNumbersThanCurrent(nums3))


#second solution
#hash table
