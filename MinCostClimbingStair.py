#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 23:34:50 2021

@author: tenor2000
"""
def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        type: List[int]
        rtype: int
        """
        # Establish array to store numbers
        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]
        # work each number from previous 2
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])