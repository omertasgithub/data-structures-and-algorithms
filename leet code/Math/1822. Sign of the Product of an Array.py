#1822. Sign of the Product of an Array
#related topics
#math

nums = [-1,-2,-3,-4,3,2,1]
nums2 = [1,5,0,2,-3]
nums3 = [-1,1,-1,1,-1]

#first solution
def arraySign(nums):
    r=1
    for i in nums:
        r*=i
    if r>0:
        return 1
    elif r<0:
        return -1
    else:
        return 0
    
print(arraySign(nums))
print(arraySign(nums2))
print(arraySign(nums3))

#Second solution
def arraySign2(nums):
    if 0 in nums:
        return 0
    i=0
    for j in nums:
        if j < 0:
            i+=1
    if i%2==0:
        return 1
    else:
        return -1
    
print(arraySign2(nums))
print(arraySign2(nums2))
print(arraySign2(nums3))