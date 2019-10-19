#https://leetcode.com/problems/set-matrix-zeroes/submissions/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #Lazy Propagation Approach! (without extra space!)
        N=len(matrix)
        if(N==0):
            return
        
        first_row=False
        first_col=False
        M=len(matrix[0])
        for i in range(N):
            for j in range(M):
                if(matrix[i][j]==0):
                    if(i==0):
                        first_row=True
                    if(j==0):
                        first_col=True
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,N):
            for j in range(1,M):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
                    
        #Check first row and first col to see if they need to be set
        if(first_col):
            for i in range(N):
                matrix[i][0]=0
                
        if(first_row):
            for i in range(M):
                matrix[0][i]=0
                        
        