class Solution:
    def getSubset(self,nums,target):
        #get a single subset with given target from array
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
            return False, []
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
        return True, firstSet
        
    def getNewArr(self,nums,currentSet,freq):
        #remove elements present in currentSet from nums
        n=len(nums)
        for ele in currentSet:
            freq[ele]-=1
        
        newArr=[] #set of indices that will be present
        for ele in nums:
            if(freq[ele]>0):
                newArr.append(ele)
                freq[ele]-=1
        
        
  
        return newArr,Counter(newArr)
        
    def usingSubsetSumLogic(self,nums,k):
        #using Subset Sum k times!  
        #Sorting in reverse is helpful!
        nums=sorted(nums,reverse=True) #SORTING IS IMPORTANT! 
        if(sum(nums)%k!=0):
            return False
            
        expectedSum=sum(nums)//k #expected_sum of each partition
        freq=Counter(nums)
        for i in range(k):
            status,currentSet=self.getSubset(nums,expectedSum)
            nums,freq=self.getNewArr(nums,currentSet,freq) #remove elements of currentSet from nums and update freq
            if(not status):
                return False
        
        return True
    def backtrack(self,idx,n,currentSum,targetSum,used,nums,k):
        if(k==1):
            return True
        if(currentSum==targetSum):
            return self.backtrack(0,n,0,targetSum,used,nums,k-1)
        
        if(currentSum>targetSum):
            return False
        for i in range(idx,n):
            if(not used[i]):
                used[i]=True
                if(self.backtrack(i+1,n,currentSum+nums[i],targetSum,used,nums,k)):
                    return True
                used[i]=False
        
        return False
                    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #backtracking solution! 
        n=len(nums)
        if(sum(nums)%k!=0):
            return False
        targetSum=sum(nums)//k #expected_sum of each partition
        used=defaultdict(lambda:False) #indices that have been used
        return self.backtrack(0,n,0,targetSum,used,nums,k)
