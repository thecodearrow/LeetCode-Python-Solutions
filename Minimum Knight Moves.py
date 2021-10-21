class Solution:
    def bfs(self,x,y):
        #Normal BFS
        queue=deque([(0,0)])
        knight_moves=[(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]
        dist=defaultdict(lambda:0)
        dist[(0,0)]=0
        visited=set()
        while queue:
            ux,uy=queue.popleft()
            if((ux,uy)==(x,y)):
                return dist[(ux,uy)]
            for dx,dy in knight_moves:
                vx=ux+dx
                vy=uy+dy
                if((vx,vy) not in visited):
                    visited.add((vx,vy))
                    dist[(vx,vy)]=dist[(ux,uy)]+1
                    queue.append((vx,vy))
                    
    def minKnightMoves(self, x: int, y: int) -> int:
        #Bidirectional BFS
        queue1=deque([(0,0)])
        queue2=deque([(x,y)])
        dist1=defaultdict(lambda:0)
        dist2=defaultdict(lambda:0)
        dist1[(0,0)]=0
        dist2[(x,y)]=0
        visited1=set()
        visited2=set()
        knight_moves=[(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]
        while queue1 and queue2:
            u1x,u1y=queue1.popleft()
            u2x,u2y=queue2.popleft()
            if((u1x,u1y) in dist2):
                return dist1[(u1x,u1y)]+dist2[(u1x,u1y)]
            if((u2x,u2y) in dist1):
                return dist1[(u2x,u2y)]+dist2[(u2x,u2y)]
            for dx,dy in knight_moves:
                v1x=u1x+dx
                v1y=u1y+dy
                v2x=u2x+dx
                v2y=u2y+dy
                if((v1x,v1y) not in visited1):
                    visited1.add((v1x,v1y))
                    dist1[(v1x,v1y)]=dist1[(u1x,u1y)]+1
                    queue1.append((v1x,v1y))
                if((v2x,v2y) not in visited2):
                    visited2.add((v2x,v2y))
                    dist2[(v2x,v2y)]=dist2[(u2x,u2y)]+1
                    queue2.append((v2x,v2y))
                    
