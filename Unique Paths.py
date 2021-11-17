class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        def countWays(i,j,n,m,dp):
            if(i==n-1 and j==m-1):
                return 1
            if(i==n or j==m):
                return 0
            key=(i,j)
            if(key in dp):
                return dp[key]
            dp[key]=countWays(i+1,j,n,m,dp)+countWays(i,j+1,n,m,dp)
            return dp[key]
        return countWays(0,0,n,m,{})
