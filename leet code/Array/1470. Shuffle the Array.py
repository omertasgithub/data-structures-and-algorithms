#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:20:24 2021

@author: omertas
"""

#related topics array

#firs solution
def shuffle(nums):
    
    mid = int(len(nums)/2)
    lst = []
    for i,j in zip(range(mid), range(mid, len(nums))):
        lst.append(nums[i])
        lst.append(nums[j])
    return lst


#better
#but doent work???
def shuffle2(nums):
    
    n = len(nums)
    res = []
    for i,j in zip(nums[:n], nums[n:]):
        res+=[i,j]
    return res
    
    