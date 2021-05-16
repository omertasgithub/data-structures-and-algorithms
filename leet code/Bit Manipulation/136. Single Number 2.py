#136. Single Number
#related topics
#hash table, bit manipulation


nums = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]

#first solution
def singleNumber(nums):
    for i,n in enumerate(nums):
        if nums.count(n)==1:
            return n
        
        
print(singleNumber(nums))
print(singleNumber(nums2))
print(singleNumber(nums3))

#second solution
#hash table


#third solution
#bit manipulation

