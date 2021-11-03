class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        heap=[(-grid[0][0],0,0)] #val,i,j #max heap! 
        visited=set()
        visited.add((0,0))
        n=len(grid)
        m=len(grid[0])
        minScore=float("inf") #maximum min value on path
        while heap:
            val,i,j=heapq.heappop(heap)
            grid[i][j]=-1
            if(i==n-1 and j==m-1):
                return -val
            dirs=[(0,1),(1,0),(0,-1),(-1,0)]
            for dx,dy in dirs:
                x,y=i+dx,j+dy
                if(x>=0 and y>=0 and x<n and y<m):
                    if((x,y) not in visited):
                        minDist=min(-val,grid[x][y])
                        heapq.heappush(heap,(-minDist,x,y))
                        visited.add((x,y))
                            
                            
                            
        
        
                        
                
                
