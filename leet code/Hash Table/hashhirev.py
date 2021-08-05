#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:31:25 2021

@author: omertas
"""

arr1 = [0,1,0,1,1,1,1,0,0,1]
k1=3
arr2 = [9,3,2,7,2,5,3,8]
k2=4



    

def isSmallestExist(arr, k):
    dic = {}

    arr.sort()
    #Since I will use dictionat i need to track location
    
    j=0
    for i in arr:
        #using ash table will make sure I will get rid of repeating elements
        if i not in dic.values():
            #j is trackign location 
            j+=1
            dic[j]=i
    #if k is greater than list then index is out of range        
    try:
        return dic[k]
    except:
        return None
    
    
        
    
print(isSmallestExist(arr1,k1))
print(isSmallestExist([5, -8, 10, 37, 101, 2, 9],6))