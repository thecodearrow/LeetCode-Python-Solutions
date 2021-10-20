class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
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
                    
