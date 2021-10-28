class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        nbrs=defaultdict(set)
        for u,v in roads:
            nbrs[u].add(v)
            nbrs[v].add(u)
        
        max_rank=0
        for i in range(n):
            for j in range(i+1,n):
                if(i!=j):
                    rank=len(nbrs[i])+len(nbrs[j])
                    if(i in nbrs[j]):
                        #directly connected
                        rank-=1
                    max_rank=max(max_rank,rank)
        
        return max_rank
