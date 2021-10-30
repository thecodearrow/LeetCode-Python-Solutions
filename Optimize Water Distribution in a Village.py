'''
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional.

Return the minimum total cost to supply water to all houses.

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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        #Add a virtual node, connect it to houses with edges weighted by the costs to build wells in these houses.
        
        #once you figure out a way to model the wells as an extra node, this problem is just a simple MST problem! 
        
        ds=DisjointSet(n+1)
        #let vertex 0 be the well node! 
        edges=[]
        for i in range(1,n+1):
            well_cost=wells[i-1]
            edges.append([0,i,well_cost])
        
        edges+=pipes
        edges=sorted(edges,key=lambda x:x[2]) 
        min_cost=0
        edge_count=0
        for u,v,c in edges:
            #pick n edges without forming a cycle! 
            if(ds.find(u)!=ds.find(v)):
                ds.union(u,v)
                min_cost+=c
                edge_count+=1
                if(edge_count==n):
                    return min_cost
            
