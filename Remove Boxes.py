class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
                    
        #https://www.youtube.com/watch?v=_8hSyaxVRZ8 (BEST EXPLAINATION)
        def getPoints(l,r,count,dp):
            if(l>r):
                return 0
            key=(l,r,count)
            if(key in dp):
                return dp[key]
            #get length of consecutive boxes starting from l
            while l+1<=r and boxes[l]==boxes[l+1]:
                count+=1 #extend count
                l+=1
            ans=(count*count)+getPoints(l+1,r,1,dp)
            for i in range(l+1,r+1):
                if(boxes[l]==boxes[i]):
                    #try to find consecutive boxes that are distant
                    midBoxesPoints=getPoints(l+1,i-1,1,dp)
                    ans=max(ans,getPoints(i,r,count+1,dp)+midBoxesPoints) #provide existing count to the distant boxes! 
                    
            dp[key]=ans
            return ans

        return getPoints(0,len(boxes)-1,1,{})
