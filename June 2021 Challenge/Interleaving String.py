#https://leetcode.com/problems/interleaving-string/
#Top Down Dp

class Solution:
    def isInterleaved(self,i,j,k,l1,l2,l3,s1,s2,s3,memo):
        if(k==l3):
            if(i==l1 and j==l2):
                return True
            return False
        key=(i,j)
        if(key in memo):
            return memo[key]
        memo[key]=False
        if(i<l1 and s1[i]==s3[k]):
            memo[key]=memo[key] or self.isInterleaved(i+1,j,k+1,l1,l2,l3,s1,s2,s3,memo)
        if(j<l2 and s2[j]==s3[k]):
            memo[key]=memo[key] or  self.isInterleaved(i,j+1,k+1,l1,l2,l3,s1,s2,s3,memo)
        
        return memo[key]
        
        
        
        
            
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        return self.isInterleaved(0,0,0,l1,l2,l3,s1,s2,s3,{})
        