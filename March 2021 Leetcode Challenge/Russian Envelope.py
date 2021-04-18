#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3690/
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes=sorted(envelopes)
        n=len(envelopes)
        dp=[1]*n
        for i in range(1,n):
            wi,hi=envelopes[i]
            for j in range(i):
                wj,hj=envelopes[j]
                if(wj<wi and hj<hi):
                    dp[i]=max(dp[i],dp[j]+1)
                    
                    
        
        return max(dp)