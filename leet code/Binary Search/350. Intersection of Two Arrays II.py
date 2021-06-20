#350. Intersection of Two Arrays II
#related topics
#hash table, two pointers, binary search, sort


nums1 = [1,2,2,1]
nums2 = [2,2]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]


#brute force
def intersect(nums1, nums2):
    def hasher(arr):
        dic = {}
        
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        return dic
    
    dic1 = hasher(nums1)
    dic2 = hasher(nums2)        
    lst = []
    for key1, value1 in dic1.items():
        for key2, value2 in dic2.items():
            if key1==key2:
                lst+=[key1]*\
                    (value1 if value1==value2 else min(value1,value2))
    return lst


print(intersect(nums1, nums2))

print(intersect(nums3, nums4))




    