#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:57:37 2021

@author: omertas
"""
arr1 = [2,7,11,15]
target1 = 9
arr2 = [2,3,4]
target2 = 6
arr3 = [1,3,5,7]
target3 = 100

def twoSum(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        curr = nums[right]+nums[left]
        if curr < target:
            left += 1
        elif curr > target:
            right -= 1
        else:
            return [left, right]
    return [-1,-1]


print(twoSum(arr1, target1))
print(twoSum(arr2, target2))
print(twoSum(arr3, target3))