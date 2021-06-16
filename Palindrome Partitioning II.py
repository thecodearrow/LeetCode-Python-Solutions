#https://leetcode.com/problems/palindrome-partitioning-ii
class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        def preComputePali():
            isPali=[[False for j in range(n)]for i in range(n)]  
            for l in range(n):
                for i in range(n-l):
                    j=i+l
                    if(s[i]==s[j]):
                        if(l<=1):
                            #length 1,2
                            isPali[i][j]=True 
                        else:
                            isPali[i][j]=isPali[i+1][j-1]
            return isPali
        
        
            
            
            
            
        isPali=preComputePali() #isPali[i:j] in O(1)
        
        #IMP only one DP state is needed!
        #cuts[i] represents the min. number of cuts for s[0 : i+1]
        cuts=[float("inf") for i in range(n)] 
        for j in range(n):
            #ending at j
            if(isPali[0][j]):
                cuts[j]=0
                continue
            for i in range(j):
                #starting at i
                if(isPali[i+1][j]):
                    #if s[i+1:j] is pali
                    #we make a cut!
                    cuts[j]=min(cuts[j],cuts[i]+1)
        
        return cuts[n-1]
                
        
        
        