#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:36:47 2021

@author: omertas
"""


#1332. Remove Palindromic Subsequences
def rem(s):
    return 2-(s==s[::-1]) - (s=='')
