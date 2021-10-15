'''
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

'''


class Graph:
    def __init__(self):
        self.nbrs=defaultdict(list)
        self.indegree=defaultdict(lambda:0)
    def initVertex(self,u):
        #initialize vertex
        self.nbrs[u]=[]
        
    def addEdge(self,u,v):
        #directed
        if(u!=v):
            self.nbrs[u].append(v)
            self.indegree[v]+=1
    
    def topoOrder(self):
        n=len(self.nbrs)
        zeroSet=[]
        for ele in self.nbrs:
            if(self.indegree[ele]==0):
                zeroSet.append(ele)
        
        topoOrder=[]
        while zeroSet:
            u=zeroSet.pop()
            topoOrder.append(u)
            for v in self.nbrs[u]:
                self.indegree[v]-=1
                if(self.indegree[v]==0):
                    zeroSet.append(v)
            
        
        if(len(topoOrder)!=n):
            #contains cycle
            return ""
        
      
        return "".join(topoOrder)
            
        

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #generate all the edges of the graph for every possible pair of words
        g=Graph()
        for w in words:
            for c in w:
                if(c not in g.nbrs):
                    g.initVertex(c)
        #if there exists a cycle, return ""
        #or else return the topological ordering
    
            
        def addEdges(word1,word2):
            l1=len(word1)
            l2=len(word2)
            l=min(l1,l2)
            i=0
            while i<l:
                c1=word1[i]
                c2=word2[i]
                if(c1!=c2):
                    break
                i+=1
        
            if(i==l and l1>l2):
                #["abc","ab"]
                return False
            g.addEdge(c1,c2) #c1 -> c2
            return True  #found a mismatching character
        
        for i in range(len(words)):
            word1=words[i]
            for j in range(i+1,len(words)):
                word2=words[j]
                if(not addEdges(word1,word2)):
                    #not possible
                    return ""
        
        topo=g.topoOrder()
     
        return topo
        
        
