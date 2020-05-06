#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        if(len(stones)==1):
            return stones[0]
        stones=[-ele for ele in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            s1=-1*heapq.heappop(stones)
            s2=-1*heapq.heappop(stones)
            rem=-1*abs(s2-s1)
            if(rem!=0):
                heapq.heappush(stones,rem)
                
        if(stones):
            return -1*stones[0]
        return 0
        
            
            
        