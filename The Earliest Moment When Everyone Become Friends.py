'''
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.


'''
class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1]*n
    def find(self,node):
        parentNode=self.parent[node]
        if(parentNode==node):
            return node
        self.parent[node]=self.find(parentNode)
        return self.parent[node]
    
    def union(self,u,v):
        leader_u,leader_v=self.find(u),self.find(v)
        if(leader_u!=leader_v):
            size_u,size_v=self.size[u],self.size[v]
            if(size_u>size_v):
                #perform swap! 
                u,v=v,u
                leader_u,leader_v=leader_v,leader_u
            self.parent[leader_u]=leader_v
            self.size[leader_v]+=self.size[leader_u]
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs=sorted(logs,key=lambda x:x[0]) #sort by timestamps
        ds=DisjointSet(n)
        for t,u,v in logs:
            ds.union(u,v)
            leader=ds.find(u)
            if(ds.size[leader]==n):
                return t
        
        return -1
            
