#https://leetcode.com/problems/maximal-square/description/

#https://www.youtube.com/watch?v=NYeVhmWsWec&t=721s

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N=len(matrix)
        if(N==0):
            return 0
        M=len(matrix[0])
        max_square_length=0
        dp=[[0 for j in range(M)]for i in range(N)]
        for i in range(N):
            for j in range(M):
                if(matrix[i][j]=='1'):
                    max_square_length=1
                    dp[i][j]=1
        for i in range(1,N):
            for j in range(1,M):
                left_cell=dp[i][j-1]
                top_cell=dp[i-1][j]
                diagonal_cell=dp[i-1][j-1]
                if(top_cell and left_cell and diagonal_cell and dp[i][j]):
                    dp[i][j]=min(diagonal_cell,top_cell,left_cell)+1
                    max_square_length=max(max_square_length,dp[i][j])
            
            
        return (max_square_length*max_square_length)
        
        
        