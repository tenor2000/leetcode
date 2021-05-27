#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:08:31 2021

@author: tenor2000

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

"""

def evalRPN(tokens):
        while True:
            for i in range(0,len(tokens)):
                if len(tokens) == 1:
                    return int(tokens[0])
                elif tokens[i] == '+':
                    tokens.insert(i+1,(int(tokens[i-2])+int(tokens[i-1])))
                    del tokens[i-2:i+1]
                    break
                elif tokens[i] == '-':
                    tokens.insert(i+1,(int(tokens[i-2])-int(tokens[i-1])))
                    del tokens[i-2:i+1]
                    break
                elif tokens[i] == '*':
                    tokens.insert(i+1,(int(tokens[i-2])*int(tokens[i-1])))
                    del tokens[i-2:i+1]
                    break
                elif tokens[i] == '/':
                    tokens.insert(i+1,(int(tokens[i-2])/int(tokens[i-1])))
                    del tokens[i-2:i+1]
                    break
                else:
                    continue