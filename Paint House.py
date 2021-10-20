
#Approach 1
class Solution:
    def getCost(self,i,n,isRed,isBlue,isGreen,costs,dp):
        if(i==n):
            return 0
        key=(i,isRed,isBlue,isGreen)
        if(key in dp):
            return dp[key]
        costR=costs[i][0]+self.getCost(i+1,n,False,True,True,costs,dp) if isRed else float("inf")
        costB=costs[i][1]+self.getCost(i+1,n,True,False,True,costs,dp) if isBlue else float("inf")
        costG=costs[i][2]+self.getCost(i+1,n,True,True,False,costs,dp) if isGreen else float("inf")
        dp[key]= min(costR,costB,costG)
        return dp[key]
    def minCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        return self.getCost(0,n,True,True,True,costs,{})
 


#Approach 2

class Solution:
    def getCost(self,i,color,n,costs,dp):
        if(i==n):
            return 0
        key=(i,color)
        if(key in dp):
            return dp[key]
        minCost=float("inf")
        for c in range(3):
             #0-Red, 1-Blue, 2-Green
            if(c!=color):
                cost=costs[i][color]+self.getCost(i+1,c,n,costs,dp) 
                minCost=min(minCost,cost)
           
        dp[key]= minCost
        return dp[key]
    def minCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        minCost=float("inf")
        for c in range(3):
            minCost=min(minCost,self.getCost(0,c,n,costs,{})) #can color first house R,G or B... obtain the best cost! 
        return minCost
        #return self.getCost1(0,n,True,True,True,costs,{})
