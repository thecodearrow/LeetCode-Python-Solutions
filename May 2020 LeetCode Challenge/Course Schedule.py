#Cycle in a directed graph!

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.neighbours=defaultdict(list)
        self.grey_set=set()
        self.black_set=set()
        
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        
    def DFS(self,node):
        if(node in self.grey_set):
            return False
        self.grey_set.add(node)
        for adjacent_node in self.neighbours[node]:
            if(adjacent_node not in self.black_set):
                return self.DFS(adjacent_node)
        self.black_set.add(node) #Mark visited!
        return True
    def isCycle(self,n):
        for node in range(n): 
            if(node not in self.black_set):
                #reset gret set
                self.grey_set=set()
                if(not self.DFS(node)):
                    return False
                
        return True
                
            

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=Graph(numCourses)
        for c1,c2 in prerequisites:
            g.addEdge(c1,c2)
        return g.isCycle(numCourses)
        