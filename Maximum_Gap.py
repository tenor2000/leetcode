#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:39:55 2021

@author: tenor2000
"""

def maximumGap(nums): 
    '''
    type: List[int]
    rtype: int
    '''
    if len(nums) < 2:
        return 0
    nums = sorted(nums)
    maxgap = 0
    for x, y in enumerate(nums):
        maxgap = max(maxgap, nums[x] - nums[x-1])
        
    return maxgap