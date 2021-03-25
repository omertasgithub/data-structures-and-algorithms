#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:43:08 2021

@author: omertas
"""

#brute force
def intersection(nums1, nums2):
    lst = []
    
    for i in set(nums1):
        if i in set(nums2):
            lst.append(i)
    return lst


#single line
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
    #below doesnt work
    # return list(set(nums1) and set(nums2))
    #because of bitwise


        
        
        
        
#Hash table     
def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    mapp = {}
    res = []
    for i in nums1:
        mapp[i] = 1
    for k in nums2:
        if k in mapp:
            res.append(k)
    
    return res


#Two pointers
nums1 = [4, 9, 5]
nums2 =  [9, 4, 9, 8, 4]
def intersection(nums1, nums2):
    i = 0
    j = 0
    res = set()
    nums1.sort()  #[4,5,9]
    nums2.sort()  #[4,4,8,9,9]
    while( i < len(nums1) and j < len(nums2) ):
        if nums1[i] < nums2[j]:
            i += 1
            continue
        if nums1[i] > nums2[j]:
            j += 1
            continue
        res.add(nums1[i])
        i += 1
        j += 1
    return res

#Binary search for simple case not for this question
def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low+high) // 2
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[high] > x:
            high = mid - 1
        else:
            return mid
    return -1