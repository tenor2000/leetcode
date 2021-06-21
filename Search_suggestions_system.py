#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:17:37 2021

@author: tenor2000
"""
def suggestedProducts(products, searchWord):
    """
    type: List[str], str
    rtype: List[List[str]]
    """
    products = sorted(products)
    storage = []
    result = []
    
    for i, char in enumerate(searchWord):
        storage = []
        for word in products:
            if searchWord[:i+1] == word[:i+1]:
                storage.append(word)
        result.append(storage[:3])
                
    return result