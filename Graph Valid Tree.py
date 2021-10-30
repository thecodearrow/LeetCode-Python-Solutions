class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,node):
        parentNode=self.parent[node]
        if(parentNode==node):
            return node
        self.parent[node]=self.find(parentNode)
        return self.parent[node]
    
    def union(self,u,v):
        leader_u,leader_v=self.find(u),self.find(v)
        if(leader_u!=leader_v):
            rank_u,rank_v=self.rank[u],self.rank[v]
            if(rank_u>rank_v):
                #perform swap! 
                u,v=v,u
                leader_u,leader_v=leader_v,leader_u
            self.parent[leader_u]=leader_v
            self.rank[leader_v]=self.rank[leader_u]+1
        
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ds=DisjointSet(n)
        #Should contain n-1 edges... should be one single component and should not contain cycles! 
        #By ensuring that there are n-1 edges, you also ensure there's only one component automatically since there are no self loops! 
       
        if(len(edges)!=n-1):
            #a tree has n-1 edges! 
            return False
        
         #only thing left is checking for cycles
        for u,v in edges:
            leader_u,leader_v=ds.find(u),ds.find(v)
            if(leader_u==leader_v):
                #contains cycle! 
                return False
            ds.union(u,v)
            
        return True
        
