#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3312/
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        if(n==0):
            return 0
        m=len(matrix[0])
        maximal=0
        for i in range(n):
            if(matrix[i][0]=='1'):
                maximal=1
                break
        for i in range(m):
            if(matrix[0][i]=='1'):
                maximal=1
                break
        dp=[[1 if(matrix[i][j]=='1') else 0 for j in range(m) ] for i in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                if(dp[i][j]):
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    maximal=max(maximal,dp[i][j])
        
        return maximal**2
                    