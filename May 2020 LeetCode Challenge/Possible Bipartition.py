"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3342/

Basically, it's asking if the graph is 2 colorable or not!

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way

"""
from collections import defaultdict
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)
    def is2Colorable(self,source,visited):
        queue=[source] 
        visited[source]=True
        color={source:0}
        while queue:
            u=queue.pop(0)
            for v in self.neighbours[u]:
                if(visited[v] and color[v]==color[u]):
                    return False,visited
                if(not visited[v]):
                    queue.append(v)
                    visited[v]=True
                    color[v]=1-color[u]
        return True,visited
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g=Graph()
        for u,v in dislikes:
            g.addEdge(u,v)
        visited=defaultdict(lambda:False)
        for i in range(1,N+1):
            if(not visited[i]):
                colorable,visited=g.is2Colorable(i,visited)
                if(not colorable):
                    return False
            
        return True
        
        