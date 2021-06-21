#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:45:51 2021

@author: omertas
"""
target1 = [1,3]
n1=3

target2 = [1,2,3]
n2 = 3

target3 = [1,2]
n3 = 4

target4 = [2,3,4]
n4 = 4
target5 = [1,3,4,6,7,8]
n5 = 9

#first solution
def buildArray(target, n):
    stack = []
    track = []
    for i in range(1,n+1):
        stack.append("Push")
        track.append(i)
        if track == target:
            break
            return stack
            
            
        
        if i not in target:
            stack.append("Pop")
            track.pop()
        
    return stack

print(buildArray(target1,n1))
print(buildArray(target2,n2))
print(buildArray(target3,n3))
print(buildArray(target4,n4))
print(buildArray(target5,n5))
print("\n")

#second solution

