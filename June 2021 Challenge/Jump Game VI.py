#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3773/

import heapq
class Solution:
    def getMaxScore(self,i,k,n,nums,memo):
        if(i==n):
            return 0
        if(i==n-1):
            return nums[i]
        if(i in memo):
            return memo[i]
        maxScore=-float("inf")
        for j in range(i+1,min(n,i+k+1)):
            currScore=self.getMaxScore(j,k,n,nums,memo)
            maxScore=max(maxScore,currScore)
        
        score=nums[i]+maxScore
        memo[i]=score
        return memo[i]
    
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        memo={}
        #return self.getMaxScore(0,k,n,nums,memo)  Top Down DP times out because of O(n*k)
        dp=nums[:]
        maxQueue=[(-nums[0],0)]
        for i in range(1,n):
            #print(maxQueue)
            while maxQueue:
                score,idx=heapq.heappop(maxQueue)
                if(i-idx<=k):
                    break
            dp[i]=nums[i]+(-score)
            heapq.heappush(maxQueue,(score,idx))
            heapq.heappush(maxQueue,(-dp[i],i))
        
        return dp[n-1]
                
        
        
    
    
        