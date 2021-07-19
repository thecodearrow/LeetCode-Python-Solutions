#https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums=sorted(nums)
        n=len(nums)
        ans=[]
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):     #duplicates!
                continue
            for j in range(i+1,n):
                if(j>i+1 and nums[j]==nums[j-1]): #duplicates!
                    continue
                l=j+1
                r=n-1
                remSum=target-(nums[i]+nums[j])
                while l<r:
                    if(nums[l]+nums[r]<remSum): 
                        l+=1
                    elif(nums[l]+nums[r]>remSum):
                        r-=1
                    else:
                        #nums[l]+nums[r]==remSum
                        
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while (l<r and nums[l]==nums[l-1]): #duplicates!
                            l+=1
                        while (l<r and nums[r]==nums[r+1]): #duplicates!
                            r-=1 
                        
                        
                        
                        
                            
        
        return ans
                    
                    