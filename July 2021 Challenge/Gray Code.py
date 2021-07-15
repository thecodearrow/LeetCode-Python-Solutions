#https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3799/

class Solution:
    def generateGreyCode(self,n):
        if(n==0):
            global ans,current
            ans.append(current)
            return
        
        self.generateGreyCode(n-1)
        #toggle ith bit
        current=current^(1<<(n-1))
        self.generateGreyCode(n-1)
        
                
    def grayCode(self, n: int) -> List[int]:
        #NOTE— current needs to be global variable for this to work! 
        global ans,current
        current=0
        ans=[]
        self.generateGreyCode(n)
        return ans
        
        