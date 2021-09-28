class Solution:                    
    #https://www.youtube.com/watch?v=_8hSyaxVRZ8 (BEST EXPLAINATION)

    #Very similar to Remove Boxes problem! 
    def strangePrinter(self, s: str) -> int:
        def getTurn(l,r,dp):
            if(l>r):
                return 0
            key=(l,r)
            if(key in dp):
                return dp[key]
            
            ans=1+getTurn(l+1,r,dp) #print chars starting from l
            for i in range(l+1,r+1):
                if(s[l]==s[i]):
                    #try to find consecutive chars that are distant
                    #print mid chars first
                    midPoints=getTurn(l+1,i-1,dp)
                    ans=min(ans,getTurn(i,r,dp)+midPoints) #provide existing count to the distant boxes! 

            dp[key]=ans
            return ans
        
    
        return getTurn(0,len(s)-1,{})
