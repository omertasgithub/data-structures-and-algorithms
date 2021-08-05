#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:16:48 2021

@author: omertas
"""


s1 = '21462675756'
s2 = '98676555533'

def Subsequent(s):
    lst = []
    for i in range(len(s)-1):
        
        if int(s[i])%2==0 and int(s[i+1])%2==0:
            lst+=s[i]+"*"
        elif int(s[i])%2==1 and int(s[i+1])%2==1:
            lst+=s[i]+"-"
        else:
            lst.append(s[i])
        
        
    return "".join(lst)+s[-1]

print(Subsequent(s1))
print(Subsequent(s2))


        
        