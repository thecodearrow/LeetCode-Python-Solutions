#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        m=len(s)
        n=len(t)
        while i<n and j<m:
            if(t[i]==s[j]):
                j+=1       
            i+=1
        
        return j==m