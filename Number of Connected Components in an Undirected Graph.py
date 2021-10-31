'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.


'''
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds=DisjointSet(n)
        for u,v in edges:
            if(ds.find(u)!=ds.find(v)):
                ds.union(u,v)
        
        leader_set=set()
        for i in range(n):
            leader=ds.find(i)
            leader_set.add(leader)
        return len(leader_set)
