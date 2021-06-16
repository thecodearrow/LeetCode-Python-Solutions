#https://leetcode.com/problems/palindrome-partitioning/solution/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
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
        def getPartitions(l,r,parts):
            if(r==n-1):
                if(isPali[l][r]):
                    parts.append(s[l:r+1])
                    ans.append(parts[:])
                    parts.pop()
                return
            
            getPartitions(l,r+1,parts)
            if(isPali[l][r]):
                #make a cut! 
                parts.append(s[l:r+1])
                getPartitions(r+1,r+1,parts)
                parts.pop()
            
            
            
            
        isPali=preComputePali()
                        
    
        
        getPartitions(0,0,[])
        return ans