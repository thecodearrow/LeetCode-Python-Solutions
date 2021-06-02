#https://leetcode.com/problems/max-area-of-island/submissions/

from collections import defaultdict,deque

class Graph:
    def __init__(self):
        self.visited=defaultdict(lambda:False)
        
    
    def isBound(self,i,j,n,m):
        if(i>=0 and j>=0):
            if(i<n and j<m):
                return True
        
        return False
    
    def bfs(self,s,n,m,grid):
        queue=deque([s])
        self.visited[s]=True
        count=0
        while queue:
            i,j=queue.popleft()
            count+=1
            down,right,up,left=(i+1,j),(i,j+1),(i-1,j),(i,j-1)
            for i,j in [down,right,up,left]:
                if(self.isBound(i,j,n,m)):
                    if(grid[i][j] and not self.visited[(i,j)]):
                        queue.append((i,j))
                        self.visited[(i,j)]=True
            
                
            
            
        
        return count
            
        
        
            
        
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        g=Graph()
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j] and not g.visited[(i,j)]):
                    #start bfs from here
                    count=g.bfs((i,j),n,m,grid)
                    ans=max(ans,count)
        return ans
        
        
        
        