class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        global ans
        ans=0
        def dfs(i,j,n,m,visited,count):
            if(i==n or j==m or i<0 or j<0):
                #out of bounds!
                return 0
            if(grid[i][j]==-1):
                #obstacle!
                return 
            if(grid[i][j]==2 and count==1):
                #ending point and valid path
                global ans
                ans+=1
                return
            key=(i,j)
            count-=1
            dirs=[(-1,0),(1,0),(0,1),(0,-1)]
            visited[(i,j)]=True
            for dx,dy in dirs:
                x,y=i+dx,j+dy
                if(not visited[(x,y)]):
                    visited[(x,y)]=True
                    dfs(x,y,n,m,visited,count)
                    visited[(x,y)]=False
            visited[(i,j)]=False
        
        
        
        
        count=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    #starting point
                    start_x,start_y=(i,j)
                if(grid[i][j]!=-1):
                    #non-obstacle
                    count+=1
        
        
        visited=defaultdict(lambda:False)
        dfs(start_x,start_y,n,m,visited,count)
        return ans
