class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #modified dijkstra! 
        heap=[(0,0,0)] #diff,i,j
        visited=set()
        n=len(heights)
        m=len(heights[0])
        diff=defaultdict(lambda: float("inf")) #min possible effort till (i,j)
        max_effort=0 #minimise max effort on path! 
        while heap:
            effort,i,j=heapq.heappop(heap) #the effort here will be minimum possible effort to get here!
            max_effort=max(max_effort,effort)
            visited.add((i,j))
            dirs=[(0,1),(1,0),(0,-1),(-1,0)]
            if(i==n-1 and j==m-1):
                return max_effort
            for dx,dy in dirs:
                x=i+dx
                y=j+dy
                if(x>=0 and y>=0 and x<n and y<m):
                    if((x,y) not in visited):
                        current_effort=abs(heights[x][y]-heights[i][j])
                        if(current_effort<diff[(x,y)]):
                            diff[(x,y)]=current_effort
                            heapq.heappush(heap,(current_effort,x,y))
        
        
                        
                
                
