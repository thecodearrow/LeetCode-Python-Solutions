#https://leetcode.com/problems/score-of-parentheses/submissions/

class Solution:
    def solve(self,start,end,s,closing):
        if(start+1==end):
            #base case
            return 1
        ans=0
        i=start+1
        while i<end:
            ans+=self.solve(i,closing[i],s,closing)
            i=closing[i]+1 #go to the next i! 
            
        return 2*ans
    def getClosing(self,s):
        #gives you the closing index for a open paren
        stack=[]
        closing={}
        for i,c in enumerate(s):
            if(c=="("):
                stack.append(i)
            else:
                open_idx=stack.pop()
                closing[open_idx]=i
        return closing
    
    def scoreOfParentheses(self, s: str) -> int:
        #add an opening and closing parens
        s="("+s
        s=s+")"
        #and then divide final ans by 2
        #this is done for cases like ()()
        n=len(s)
        closing=self.getClosing(s) 
        score=self.solve(0,n-1,s,closing)//2
        return score
        
                
        
                