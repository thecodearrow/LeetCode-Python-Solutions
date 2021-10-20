class Solution:
    def getCost(self,i,color,n,k,costs,dp):
        if(i==n):
            return 0
        key=(i,color)
        if(key in dp):
            return dp[key]
        minCost=float("inf")
        for c in range(k):
            if(c!=color):
                currentCost=costs[i][color]+self.getCost(i+1,c,n,k,costs,dp) #cost of painting neighbour with color c
                minCost=min(minCost,currentCost)

        dp[key]=minCost
        return dp[key]
    def minCostII(self, costs: List[List[int]]) -> int:
        n=len(costs)
        k=len(costs[0])
        minCost=float("inf")
        for c in range(k):  
            currentCost=self.getCost(0,c,n,k,costs,{}) #cost painting first house with color c
            minCost=min(minCost,currentCost)
        return minCost
        
        
