class Solution:
    def canSplit(self,i,n,s,wordSet,dp):
        #O(n^3) including creating substring (current+=s[j])
        if(i==n):
            return True
        if(i in dp):
            return dp[i]
        canBreak=False
        current=""
        for j in range(i,n):
            current+=s[j]
            if(current in wordSet):
                if(self.canSplit(j+1,n,s,wordSet,dp)):
                    canBreak=True
                    break
            
        dp[i]=canBreak
        return dp[i]
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        n=len(s)
        current=""
        return self.canSplit(0,n,s,wordSet,{})
