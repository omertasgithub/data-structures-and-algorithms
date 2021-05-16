#1748. Sum of Unique Elements
#related topics
#array, hashtable

nums = [1,2,3,2]
nums2 = [1,1,1,1,1]
nums3 = [1,2,3,4,5]
#first solution
def sumofUnique(nums):
    total = 0
    for i,n in enumerate(nums):
        if nums.count(n)==1:
            total+=n
    return total

print(sumofUnique(nums))
print(sumofUnique(nums2))
print(sumofUnique(nums3))

#One line #check later
def sumOfUnique(self, A):
        return sum(a for a, c in collections.Counter(A).items() if c == 1)
    
    
#check
return sum(filter(lambda x: nums.count(x)==1, nums))