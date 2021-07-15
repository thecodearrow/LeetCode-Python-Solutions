#https://leetcode.com/problems/redundant-connection/

class DisjointSet:
    def __init__(self):
        n=1000
        self.elements=[{"rank":0,"parent":i} for i in range(n+1)]
    
    def findSet(self,node):
        current=node
        parent=self.elements[node]["parent"]
        if(current==parent):
            return current
        self.elements[current]["parent"]=self.findSet(parent)
        return self.elements[current]["parent"]
    
    def union(self,u,v):
        leader_u=self.findSet(u)
        leader_v=self.findSet(v)
        rank_u=self.elements[leader_u]["rank"]
        rank_v=self.elements[leader_v]["rank"]
        if(rank_u>=rank_v):
            #promote leader_u 
            if(rank_u==rank_v):
                #increment rank by 1! 
                self.elements[leader_u]["rank"]+=1
            self.elements[leader_v]["parent"]=leader_u
        else:
            #promote leader_v 
            self.elements[leader_u]["parent"]=leader_v
            
            
            
            

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds=DisjointSet()
        ans=None
        for u,v in edges:
            l_u=ds.findSet(u)
            l_v=ds.findSet(v)
            #print(u,v,l_u,l_v)
            if(l_u==l_v):
                #redundant! 
                ans=[u,v]
            else:
                ds.union(u,v)
        #print(ds.elements[:6])
        return ans
            