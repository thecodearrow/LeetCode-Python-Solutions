#https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):

        index={}
        i=-1
      
        for ele in nums:
            i+=1
            idx1=i
            one=ele
            two=target-ele
            if(two in index):
                idx2=index[two]
                return([idx1,idx2])
                break 
            index[ele]=i
            
            
            