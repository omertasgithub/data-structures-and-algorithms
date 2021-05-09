#1848. Minimum Distance to the Target Element
#realted topics
#array


nums = [1,2,3,4,5,5,5]
target = 5
start = 3
nums2 = [1] 
target2 = 1
start2 = 0
nums3 = [1,1,1,1,1,1,1,1,1,1]
target3 = 1
start3 = 0
def getMinDistance(nums, target, start):
    lst = []
    for i,j in enumerate(nums):
        if j==target:
            lst.append(abs(start-i))
    return min(lst)

print(getMinDistance(nums, target, start))
print(getMinDistance(nums2, target2, start2))
print(getMinDistance(nums3, target3, start3))