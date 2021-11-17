class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        def countWays(i,j,n,m,dp):
            if(i==n or j==m):
                #out of bounds!
                return 0
            if(obstacleGrid[i][j]==1):
                #obstacle! 
                return 0
            if(i==n-1 and j==m-1):
                return 1 
           
            
                
            key=(i,j)
            if(key in dp):
                return dp[key]
            dp[key]=countWays(i+1,j,n,m,dp)+countWays(i,j+1,n,m,dp)
            return dp[key]
        return countWays(0,0,n,m,{})
