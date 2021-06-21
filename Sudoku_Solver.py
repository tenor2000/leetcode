#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:53:44 2021

@author: tenor2000
"""
def solveSudoku(board):
        """
        type: List[List[str]
        Do not return anything, modify board in-place instead.
        """
        def find_next_space(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        return r,c
            
            # if there are no more empty spaces       
            return None, None
            
        def is_valid(i, j, guess, board): 
            row = board[i]
            column = [board[x][j] for x in range(9)]
            box = []
            # find the start index for the row by using floor division
            row_start = (i//3) * 3
            # find the start index for the column by using floor division
            col_start = (j//3) * 3
            # range wi be the 3 indices of row 
            for r in range(row_start, row_start+3):
                # range will be the 3 indices of the column
                for c in range(col_start, col_start+3):
                    box.append(board[r][c])

            if str(guess) in row or str(guess) in column or str(guess) in box:
                return False

            return True
        
        def solve(board):
            row, col = find_next_space(board)
            
            if row is None:
                return True
        
            for guess in range(1,10):
                if is_valid(row, col, guess, board):
                    board[row][col] = str(guess)
                    if solve(board):
                        return True
                board[row][col] = "."
            
            return False
        
        solve(board)
        for x in board:
            print(x)
            
board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

if __name__ == '__main__':
    for x in board:
        print(x)
    print("")
    solveSudoku(board)