#https://leetcode.com/problems/play-with-chips/
class Solution(object):
    def calculateDist(self,pos1,pos2):
        diff=abs(pos1-pos2)
        if(diff%2==0):
            return 0
        return 1
    def minCostToMoveChips(self, chips):
        answer=float("inf")
        positions=[]
        for p in chips:
            positions.append(p)
        for pos in positions:
            #cost to pos from ele
            cost=0
            for currentPos in chips:
                cost+=self.calculateDist(currentPos,pos)
            
            answer=min(answer,cost)
            
        return answer
                
        
        