#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:14:59 2021

@author: tenor2000
"""
def maxAreaOfIsland(grid):
    """
    type: List[List[int]]
    rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    
    # visited is making an identical grid of falses which will then turn each square true when checked
    visited = [[False]*n for i in range(m)]
    
    # edge shows the possible coordinates relative to the target location (0,1),(1,0),(0,-1), (-1,0)
    edge = [0, 1, 0, -1, 0]
    
    # depth first search (or traversal) to calculate area starting from each cell recursion
    def dfs(r, c):
        # statement won't add into area because it is either end of column, end of row, not a 'land', or already been checked
        if r < 0 or r==m or c < 0 or c ==n or grid[r][c] == 0 or visited[r][c] == True:
            return 0
        area = 1
        
        # this step basically sets the coordinate to "visited" so will be ignored if checked later (see above)
        visited[r][c] = 1
        
        # calculate area for all 4 possible direction(0, 1), (0, -1), (1, 0), (-1, 0) of a cell and total is sum of all these
        for i in range(4):
            # this will branch out recursively to check each non false coordinate around it and then add it up.
            area += dfs(r+edge[i], c+edge[i+1])
        # this will be used later to compare this island area vs the highest current result
        return area
        
    result  = 0
    
    # starts search at (0,0)
    for i in range(m):
        for j in range(n):
            #the dfs searches and adds up the area around the coordinate
            result = max(result, dfs(i, j))
    
    return result