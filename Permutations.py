#https://leetcode.com/problems/permutations/description/

#MIGHT CONTAIN DUPLICATES

#https://leetcode.com/problems/permutations-ii/description/

#GOD LEVEL EXPLAINATION https://www.youtube.com/watch?v=nYFd7VHKyWQ&t=83s



from collections import defaultdict
class Solution:
    def permute(self, nums):
        
        count=defaultdict(lambda:0)

        for n in nums:
            count[n]+=1
    

        resultList=[]
        result=[0 for i in range(len(nums))] #used to store every possible permutation 
        level=0
        self.performPermute(nums,count,level,result,resultList)
        return resultList



    def performPermute(self,arr,count,level,result,resultList):
        if(level>=len(arr)):
            newP=list((result))
            resultList.append(newP)
            return 

        for ele in count.keys():
            if(count[ele]==0):
                continue
            result[level]=ele 
            count[ele]-=1
            self.performPermute(arr,count,level+1,result,resultList)
            count[ele]+=1 





