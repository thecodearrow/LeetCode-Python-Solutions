#https://leetcode.com/problems/sudoku-solver/submissions/

class Solution(object):
    def isValid(self,sudoku,row,col,value):
        #Check if value is present in col
        for i in range(9):
            if(sudoku[i][col]==value):
                return False
        #Check if value is present in row
        for i in range(9):
            if(sudoku[row][i]==value):
                return False
           
        #Check if value is present in box
        if(0<=row<=2):
            x=0
        elif(3<=row<=5):
            x=3
        elif(6<=row<=8):
            x=6
            
        if(0<=col<=2):
            y=0
        elif(3<=col<=5):
            y=3
        elif(6<=col<=8):
            y=6
        
        for i in range(x,x+3):
            for j in range(y,y+3):
                if(sudoku[i][j]==value):
                    return False
        return True
    
   
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def sudokuSolver(row,col):
            if(row==9):
                return True
            if(col==9):
                return sudokuSolver(row+1,0)

            if(row<=8 and col<=8):
                if(board[row][col]=="."):
                    for number in range(1,10):
                        if(self.isValid(board,row,col,str(number))):
                            board[row][col]=str(number)
                            if(sudokuSolver(row,col+1)):
                                return True
                            board[row][col]="."
                    return False
                else:
                    return sudokuSolver(row,col+1)

                    
                
            
        
        sudokuSolver(0,0)
        