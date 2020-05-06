#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3311/

class Solution:
    def lcs(self,s1,s2,m,n,l1,l2,cache):
        if(m>=l1 or n>=l2):
            return 0
        if(cache[m][n]!=-1):
            return cache[m][n]
        if(s1[m]==s2[n]):
            return 1+self.lcs(s1,s2,m+1,n+1,l1,l2,cache)
        lcs1=self.lcs(s1,s2,m+1,n,l1,l2,cache)
        lcs2=self.lcs(s1,s2,m,n+1,l1,l2,cache)
        cache[m][n]=max(lcs1,lcs2)
        return cache[m][n]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache=[[-1 for i in range(len(text2))] for j in range(len(text1))]
        return self.lcs(text1,text2,0,0,len(text1),len(text2),cache)