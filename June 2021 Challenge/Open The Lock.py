#https://leetcode.com/problems/open-the-lock/submissions/

from collections import defaultdict,deque
class Solution:
    def listToString(self,a):
        s=""
        for i in a:
            s+=str(i)
        return s
    
    def stringToList(self,s):
        #assuming valid string! 
        l=[]
        for c in s:
            l.append(int(c))
        
        return l
    
    def getNeighbours(self,a):
        nbrs=[]
        
        for i in range(len(a)):
            n=a[:]
            n[i]=(a[i]+1)%10 #+1
            nbrs.append(n[:])
            n[i]=a[i] #change it back
            n[i]=(a[i]-1)%10 #-1
            nbrs.append(n[:])
        
        return nbrs
                
            
            
    def openLock(self, deadends: List[str], target: str) -> int:
        source="0000"
        queue=deque([[0,0,0,0]])
        deadends=set(deadends)
        visited=defaultdict(lambda:False)
        visited[source]=True
        turns={}
        turns[source]=0
        if(source in deadends):
            return -1
        while queue:
            u=queue.popleft()
            u_string=self.listToString(u)
            if(u_string==target):
                return turns[target]
            for v in self.getNeighbours(u):
                v_string=self.listToString(v)
                if(not visited[v_string] and v_string not in deadends):
                    visited[v_string]=True
                    turns[v_string]=turns[u_string]+1
                    queue.append(v)
        
        return -1
                
            
            
            
            