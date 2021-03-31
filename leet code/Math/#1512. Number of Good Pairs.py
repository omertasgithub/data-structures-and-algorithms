
#1512. Number of Good Pairs

#array, math, hash table

nums = [1,2,3,1,1,3]
nums2 = [1,1,1,1]
nums3 = [1,2,3]
#(0,3)  (0,4) 

# first solution brute force
def numIdenticalPairs(nums):
    output = 0
    for i,n in enumerate(nums):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j] and i < j:
                output += 1
    return output

print(numIdenticalPairs(nums))
print(numIdenticalPairs(nums2))
print(numIdenticalPairs(nums3))


#[1,2,3,1,1,3] - [1,2,3,1,1,3] 

#hash table
hashMap = {}
res = 0
for number in nums:            
    if number in hashMap:
        res += hashMap[number]
        hashMap[number] += 1
    else:
        hashMap[number] = 1


