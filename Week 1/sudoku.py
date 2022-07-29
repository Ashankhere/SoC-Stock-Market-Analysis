# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:49:04 2022

@author: ashan
"""

N = 9   #size of sudoku nxn
   
def sudoku_solve(arr):
    
    l=[0,0] 
    if (empty_locations(arr, l)):
        return True
     
    row = l[0]
    col = l[1]

    for num in range(1, N+1):
         
        if(check_location_is_safe(arr, row, col, num)):

            arr[row][col]= num

            if(sudoku_solve(arr)):
                return True

            arr[row][col] = 0

    return False
    
def empty_locations(arr, l):
    for i in range(N):
        for j in range(N):
            if(arr[i][j]== 0):
                l[0]= i
                l[1]= j
                return False
    return True

def check_location_is_safe(arr, row, col, num):
    
    def row_check(arr, row, num):
        for i in range(N):
            if(arr[row][i] == num):
                return False
        return True
    
    def col_check(arr, col, num):
        for i in range(N):
            if(arr[i][col] == num):
                return False
        return True
    
    def box_check(arr, row, col, num):
        for i in range(int(N/3)):
            for j in range(3):
                if(arr[i + row][j + col] == num):
                    return False
        return True

    return row_check(arr, row, num) and col_check(arr, col, num) and box_check(arr, row - row % int(N/3), col - col % 3, num)

def print_grid(arr):
    for i in range(N):
        print (" ")
        for j in range(N):
            print (arr[i][j], end =" ")


def sudoku_check2(arr,row,col):
    
    def row_check(arr, row):
            a = []
            for i in range(N):
                if arr[row][i] in a:
                    return False
                if arr[row][i] != 0:
                    a.append(arr[row][i])
            return True
            
    def column_check(arr, col):
            a = []
            for i in range(N):
                if arr[i][col] in a:
                    return False
                if arr[i][col] != 0:
                    a.append(arr[i][col])
            return True
            
    def box_check(arr, row2, col2): 
            a = []                      
            for i in range(int(N/3)):
                for j in range(3):
                    if arr[i + row2][j + col2] in a:
                        return False
                    if arr[i + row2][j + col2] != 0:
                        a.append(arr[i + row2][j + col2])
            return True
    
    return (row_check(arr, row) and column_check(arr, col) and box_check(arr, row - row % int(N/3), col - col % 3))

def sudoku_validity(arr):
    
    for i in range(N):
        for j in range(N):
            if not sudoku_check2(arr,i,j):
                return False
    return True
        

grid = [          [0, 1, 5, 0, 0, 2, 8, 0, 9],
                  [0, 0, 0, 0, 0, 1, 6, 0, 7],
                  [0, 7, 0, 0, 0, 8, 4, 0, 0],
                  [0, 0, 6, 0, 1, 7, 0, 4, 5],
                  [0, 5, 3, 0, 0, 4, 7, 0, 0],
                  [8, 4, 0, 0, 9, 5, 0, 6, 2],
                  [0, 0, 4, 1, 7, 0, 0, 8, 6],
                  [7, 6, 0, 5, 2, 0, 9, 1, 0],
                  [5, 9, 1, 0, 8, 6, 0, 0, 0]];

if (sudoku_validity(grid)):
    print("correct sudoku")    
    if(sudoku_solve(grid)):
        print_grid(grid)
    else:
        print ("But No solution exists")
else:
    print("sudoku not correct")

