#1389. Create Target Array in the Given Order
#related topics
#array


nums = [0,1,2,3,4]
index = [0,1,2,2,1]
nums2 = [1,2,3,4,0]
index2 = [0,1,2,3,0]
nums3 = [1]
index3 = [0]  

#first solution
def createTargetArray(nums, index):
    res = []
    for i,j in zip(index,nums):
        res.insert(i,j)
    return res

print(createTargetArray(nums, index))
print(createTargetArray(nums2, index2))
print(createTargetArray(nums3, index3))

#second solution
def createTargetArray2(nums, index):
     arr = []
     for n,i in zip(nums,index): 
         arr[i:i] = [n]
     return arr
 
print(createTargetArray2(nums, index))
print(createTargetArray2(nums2, index2))
print(createTargetArray2(nums3, index3))
