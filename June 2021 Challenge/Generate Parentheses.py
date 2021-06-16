#https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
    def generateParens(self,i,n,left,right,current):
        #backtracking mindfully! 
        if(i==2*n):
            global ans
            pString="".join(current)
            ans.append(pString)
            return
        if(left<n):
            self.generateParens(i+1,n,left+1,right,current+["("])
        if(right<left):
            #right has to catch up to left
            self.generateParens(i+1,n,left,right+1,current+[")"])
            
            
    def generateParenthesis(self, n: int) -> List[str]:
        global ans
        ans=[]
        self.generateParens(0,n,0,0,[])
        return ans