#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3768/
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers=[(s,e) for s,e in zip(speed,efficiency)] 
        engineers=sorted(engineers,key=lambda x: x[1],reverse=True) #decreasing order of e
        speeds=[]
        ans=0
        current_sum=0
        for s,e in engineers:
            #consider this as min_e engineeer!
            if(len(speeds)==k):
                #kick out the one with the min speed! 
                current_sum-=heapq.heappop(speeds)
            heapq.heappush(speeds,s)
            current_sum+=s
            ans=max(e*current_sum,ans) #handles <=k
            
        MOD=10**9+7
        return ans%(MOD)
            
        