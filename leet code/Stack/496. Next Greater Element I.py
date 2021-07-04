#496. Next Greater Element I
#realted topics
#hash table, stack

nums1 = [4,1,2]
nums2 = [1,3,4,2]

#firs solution

def nextGreaterElement(nums1, nums2):
    cache, st = {}, []

    for x in nums2:
        while st and st[-1]<x:
            cache[st.pop()]=x
        st.append(x)
            
    result = [-1] * len(nums1)
    for idx, x in enumerate(nums1):
        if x in cache:
            result[idx] = cache[x]
    return result

#second solution iwth get function
 
def nextGreaterElement(nums1, nums2):
    cache, st = {}, []

    for x in nums2:
        while st and st[-1]<x:
            cache[st.pop()]=x
        st.append(x)
    result = []     
    for x in nums1:
        result.append(cache.get(x,-1))
    return result

print(nextGreaterElement(nums1, nums2))

#third solution with helper


def nextGreaterElement(self, findNums, nums):
        def helper(num):
            for tmp in nums[nums.index(num):]:
                if tmp > num:
                    return tmp
            return -1

        return map(helper, findNums)
        