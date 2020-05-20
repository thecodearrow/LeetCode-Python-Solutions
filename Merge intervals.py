#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0]) #sorting by start
        result=[]
        for si,ei in intervals:
            if(result and si<=result[-1][1]):
                #overlap exists
                result[-1][1]=max(result[-1][1],ei) #update end
            else:
                result.append([si,ei])
        
        return result