class Solution:
    def getFirstSubset(self,nums,target):
        #O(N*Target)
        n=len(nums)
        nums=[0]+nums #1-indexing
        dp=[[False for j in range(target+1)] for i in range(n+1)]
        for i in range(n):
            dp[i][0]=True
        for i in range(1,n+1):
            for j in range(1,target+1):
                if(j-nums[i]>=0):
                    dp[i][j]=dp[i][j] or dp[i-1][j-nums[i]] #include
                dp[i][j]=dp[i][j] or dp[i-1][j] #don't include 
                
        
        if(not dp[n][target]):
            return []
        #now track back the set from DP matrix
        j=target
        i=n
        firstSet=[]
        while i>0:
            if(not dp[i-1][j]):
                #dp[i-1][j] is False, ele has to be there! 
                firstSet.append(nums[i]) 
                j=j-nums[i]
            i-=1
        return firstSet
        
        
    def canPartition(self, nums: List[int]) -> bool:
        expectedSum=sum(nums)//2
        if(sum(nums)%2!=0):
            return False
        
        n=len(nums)
        count=Counter(nums)
        #find a single subset! 
        firstSet=self.getFirstSubset(nums,expectedSum)
        print(firstSet)
        #now remove elements that are from firstSet in nums and try to find secondSet (if possible!)
        for ele in firstSet:
            count[ele]-=1
        
        secondSetSum=0
        for ele in nums:
            if(count[ele]>0):
                secondSetSum+=ele
                count[ele]-=1 #we use it once! 
        return secondSetSum==expectedSum
