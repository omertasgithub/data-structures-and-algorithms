#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:19:04 2021

@author: omertas
"""


#480. Running Sum of 1d Array

#Array 

#Brute force
nums = [1,2,3,4]
def runsum1(nums):
    lst = []
    for i in range(len(nums)):
        tot = sum(nums[0:(i+1)])
        lst.append(tot)
    return lst



#One line bruter 
def runsum2(nums):
    return [i for i in [sum(nums[0:(j+1)]) for j in range(len(nums))]]

#Built oh no

from itertools import accumulate

def runsum3(nums):
    return accumulate(nums)
