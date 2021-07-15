##https://leetcode.com/problems/max-consecutive-ones-iii/submissions/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            start=0
            end=0
            flipped=0
            n=len(nums)
            maxChain=0
            while start<n and end<n:
                if(nums[end]==0):
                    if(flipped<k):
                        flipped+=1
                    else:
                        while nums[start]!=0:
                            start+=1
                        start+=1
                end+=1
                maxChain=max(maxChain,end-start)
            return maxChain

            

                
                
        