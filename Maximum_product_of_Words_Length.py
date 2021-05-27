#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:21:42 2021

@author: tenor2000

Maximum Product of Word Lengths

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.

If no such two words exist, return 0.

"""

def maxProduct(words):
    highest = 0
    for i in range(0,len(words)):
        for j in range(i+1,len(words)):
            if bool(set(words[i]) & set(words[j])) == False:
                highest = max(highest,len(words[i]) * len(words[j]))  
    return highest