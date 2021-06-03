#https://leetcode.com/problems/interleaving-string/
#Top Down Dp

class Solution:
    def isInterleaved(self,i,j,k,l1,l2,l3,s1,s2,s3,memo):
        if(k==l3):
            if(i==l1 and j==l2):
                return True
            return False
        
        if(memo[i][j] is not None):
            #exists! 
            return memo[i][j]
        memo[i][j]=False
        if(i<l1 and s1[i]==s3[k]):
            memo[i][j]=memo[i][j] or self.isInterleaved(i+1,j,k+1,l1,l2,l3,s1,s2,s3,memo)
        if(j<l2 and s2[j]==s3[k]):
            memo[i][j] = memo[i][j] or  self.isInterleaved(i,j+1,k+1,l1,l2,l3,s1,s2,s3,memo)
        
        return memo[i][j]
        
        
        
        
            
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        memo=[[None for j in range(l2+1)] for i in range(l1+1)]
        return self.isInterleaved(0,0,0,l1,l2,l3,s1,s2,s3,memo)
        