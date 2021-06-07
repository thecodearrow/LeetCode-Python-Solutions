#https://leetcode.com/problems/min-cost-climbing-stairs/submissions/

class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #O(N) time, O(1) space! 
        n=len(cost)
        prev=0
        prev_prev=0
        for i in range(2,n+1):
            c1=cost[i-1]+prev
            c2=cost[i-2]+prev_prev
            prev_prev=prev
            prev=min(c1,c2)
        
        return prev
            