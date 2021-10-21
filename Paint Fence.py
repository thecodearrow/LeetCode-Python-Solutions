class Solution:
    def countWays(self,i,k,dp):
        if(i==0):
            return k
        if(i==1):
            return k*k
        if(i in dp):
            return dp[i]
        dp[i]=(k-1)*(self.countWays(i-1,k,dp)+self.countWays(i-2,k,dp))
        return dp[i]
        
        
    def numWays(self, n: int, k: int) -> int:
        #return self.countWays(n-1,k,{}) 
        if(n==1):
            return k
        ways=[0]*(n)
        ways[0]=k
        ways[1]=k*k
        for i in range(2,n):
            ways[i]=(k-1)*(ways[i-1]+ways[i-2])
        return ways[n-1]
        
        
        
