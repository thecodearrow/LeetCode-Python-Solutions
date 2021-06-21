#https://leetcode.com/problems/swim-in-rising-water/

#https://www.youtube.com/watch?v=dmP65LPl9wQ 


#can  be solved using binary search or heaps! 


import heapq
class Solution:
    def solution1(self,grid):
        #Min-heap approach
        n=len(grid)
        visited=[[False for j in range(n)] for i in range(n)]
        visited[0][0]=True
        heights=[(grid[0][0],0,0)]
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        while heights:
            time,i,j=heapq.heappop(heights)
            if(i==n-1 and j==n-1):
                return time
            for x,y in dirs:
                nI,nJ=i+x,j+y
                if(nI<0 or nJ<0 or nI==n or nJ==n or visited[nI][nJ]):
                    #invalid! 
                    continue
                h=max(grid[nI][nJ],time) #ensure we keep track of max. time! 
                heapq.heappush(heights,(h,nI,nJ))
                visited[nI][nJ]=True
    
    def isValid(self,i,j,n):
        if(i<0 or j<0 or i>=n or j>=n):
            return False
        return True
    def isPossible(self,grid,time):
        #is it possible to visit (n-1,n-1) in time t
        if(grid[0][0]>time):
            return False
        n=len(grid)
        queue=deque([(0,0)])
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=defaultdict(lambda:False)
        visited[(0,0)]=True
        while queue:
            i,j=queue.popleft()
            if(i==n-1 and j==n-1):
                #reached 
                return True
            for x,y in dirs:
                ni,nj=i+x,j+y
                if(not visited[(ni,nj)] and self.isValid(ni,nj,n)):
                    if(grid[ni][nj]<=time):
                        visited[(ni,nj)]=True
                        queue.append((ni,nj))
        return False
    def solution2(self,grid):
        #binary search
        high=3500
        low=0
        ans=float("inf")
        while low<=high:
            mid=(low+high)//2
            if(self.isPossible(grid,mid)):
                ans=min(ans,mid)
                high=mid-1 #try to minimise further! 
            else:
                low=mid+1
        
        return ans
        
        
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Min-heap approach
        return self.solution1(grid)
            
        
        
        