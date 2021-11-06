class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def dist(coord1,coord2):
            x1,y1=coord1
            x2,y2=coord2
            return abs(x1-x2)+abs(y1-y2)
        
        total_cost=0
        d_first=float("inf") 
        for nut in nuts:
            d=dist(nut,tree)
            d_first=min(d_first,dist(squirrel,nut)-dist(nut,tree))
            total_cost+=(2*d) #tree to nut, nut to tree
        
        return total_cost+d_first
        
        
