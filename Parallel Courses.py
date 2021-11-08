class Graph:
    def __init__(self):
        self.nbrs=defaultdict(list)
        self.indegree=defaultdict(lambda:0)
    def addEdge(self,u,v):
        #directed
        self.nbrs[u].append(v)
        self.indegree[v]+=1
    def getSemCount(self,n):
        #use Kahn's + BFS to calculate semesters
        zeroSet=[]
        for i in range(1,n+1):
            if(self.indegree[i]==0):
                zeroSet.append(i)
        
        sems=0
        vertices_visited=0
        topo=[]
        s=0
        while s<len(zeroSet):
            l=len(zeroSet)
            for i in range(s,l):
                u=zeroSet[i]
                vertices_visited+=1
                for v in self.nbrs[u]:
                    self.indegree[v]-=1
                    if(self.indegree[v]==0):
                        zeroSet.append(v)
            
            s=l #update starting point for next level! 
            sems+=1 #level wise! 
        
        if(vertices_visited!=n):
            #cycle
            return -1
        return sems
    
        
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g=Graph()
        for u,v in relations:
            g.addEdge(u,v) #prev to next
        sems=g.getSemCount(n)
        return sems
