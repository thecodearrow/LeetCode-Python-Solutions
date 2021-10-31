'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        ds=DisjointSet(n)
        for u,v in pairs:
            ds.union(u,v)
        
        components=defaultdict(list)
        for i in range(n):
            leader=ds.find(i)
            components[leader].append(s[i]) #adding the chars directly
        
        for l in components:
            components[l]=sorted(components[l],reverse=True) #sort it
        
        ans=['']*n
        for i in range(n):
            l=ds.find(i)
            ans[i]=components[l].pop()
        
            
        return "".join(ans)
        
