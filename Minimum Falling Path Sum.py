class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def minPathSum(i,j,n,dp):
            if(i==n):
                return 0
            if(j<0 or j==n):
                return float("inf")
            key=(i,j)
            if(key in dp):
                return dp[key]
            down=minPathSum(i+1,j,n,dp)
            diag1=minPathSum(i+1,j-1,n,dp)
            diag2=minPathSum(i+1,j+1,n,dp)
            dp[key]=matrix[i][j]+min(down,diag1,diag2)
            return dp[key]
        
        ans=float("inf") #min path sum
        n=len(matrix) 
        dp={} #GLOBAL MEMO vs LOCAL MEMO (IMP! )
        for c in range(n): 
            #start from first row
            #ps=minPathSum(0,c,n,{}) #using a local memo (SLOW)
            ps=minPathSum(0,c,n,dp) #using a global memo
            ans=min(ps,ans)
        return ans
