class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        #multi source bfs
        INF=2**31-1
        n=len(rooms)
        m=len(rooms[0])
        queue=deque() #add all gates
        visited=set()
        for i in range(n):
            for j in range(m):
                if(rooms[i][j]==0):
                    #gates
                    queue.append((i,j,0))
                    visited.add((i,j))
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            i,j,d=queue.popleft()
            for dx,dy in dirs:
                x,y=i+dx,j+dy
                if(x>=0 and y>=0 and x<n and y<m):
                    if(rooms[x][y]==INF and (x,y) not in visited):
                        #a room that's not visited! 
                        rooms[x][y]=d+1
                        queue.append((x,y,d+1))
                        visited.add((x,y))
            
            
        
