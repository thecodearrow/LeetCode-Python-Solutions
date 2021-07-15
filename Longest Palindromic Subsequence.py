#https://leetcode.com/problems/longest-palindromic-subsequence/submissions/


'''
You can also solve this using LCS (s, reverse(s))

or 

You can also solve this bottom-up by constructing the DP table diagonally, legth wise (similar to isPali[i:j] )



'''
class Solution:
    def lps(self,s):
        #filling the table diagonally, length-wise!
        n=len(s)
        dp=[[0 for j in range(n)] for i in range(n)]
        
        for i in range(n):
            dp[i][i]=1
            
        for l in range(1,n):
            for i in range(n-l):
                j=i+l
                if(s[i]==s[j]):
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
                
        
        return dp[0][n-1]
    
    def lcs(self,i,j,n,s1,s2,dp):
        if(i==n):
            return 0
        if(j==n):
            return 0
        key=(i,j)
        if(key in dp):
            return dp[key]
        if(s1[i]==s2[j]):
            dp[key]= 1+self.lcs(i+1,j+1,n,s1,s2,dp)
        else:
            c1=self.lcs(i+1,j,n,s1,s2,dp)
            c2=self.lcs(i,j+1,n,s1,s2,dp)
            dp[key]=max(c1,c2)
        
        return dp[key]
    def longestPalindromeSubseq(self, s: str) -> int:
        #return self.lps(s)
        
        return self.lcs(0,0,len(s),s,s[::-1],{})