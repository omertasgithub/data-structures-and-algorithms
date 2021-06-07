#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 14:02:24 2021

@author: omertas
"""

nums = [1,1,2,2,2,3]
nums2 = [2,3,1,3,2]
nums3 = [-1,1,-6,4,5,-6,1,4,1]
def frequencySort(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    dic_ord = sorted(dic.items(), key=lambda x:(x[1],-x[0]))
    lst = []
    for i in dic_ord:
        lst+= [i[0]]*i[1]
    return lst

print(frequencySort(nums))
print(frequencySort(nums2))
print(frequencySort(nums3))


def frequencySort(self, A):
    import collections
    count = collections.Counter(A)
    return sorted(A, key=lambda x: (count[x], -x))
    