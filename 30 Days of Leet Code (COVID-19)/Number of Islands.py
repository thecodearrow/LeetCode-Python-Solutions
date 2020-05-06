#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/

#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/

from collections import defaultdict
class Graph:
    def __init__(self):
        self.nbrs=defaultdict(list)
        self.visited=defaultdict(lambda:False)
    def addEdge(self,u,v):
        self.nbrs[u].append(v)
        self.nbrs[v].append(u)
    
  
    def BFS(self,s):
        queue=[s]
        while queue:
            u=queue.pop(0)
            for v in self.nbrs[u]:
                if(not self.visited[v]):
                    self.visited[v]=True
                    queue.append(v)
        
        
    

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        if(m==0):
            return 0
        n=len(grid[0])
        g=Graph()
        for i in range(m):
            for j in range(n):
                e=(i,j)
                if(grid[i][j]=="1"):
                    if(i<m-1 and grid[i+1][j]=="1"):
                        e1=(i+1,j)
                        g.addEdge(e,e1)
                    if(j<n-1 and grid[i][j+1]=="1"):
                        
                        e2=(i,j+1)
                        g.addEdge(e,e2)
                        
        islands=0
        for i in range(m):
            for j in range(n):
                e=(i,j)
                if(grid[i][j]=="1" and not g.visited[e]):
                    islands+=1
                    g.BFS(e)
                    
        return islands
                    
                        
                                 
        
        
                
                
        
        