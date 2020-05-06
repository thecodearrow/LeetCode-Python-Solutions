#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/

class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        if(n==0):
            return True
        stack=[]
        stars=[]
        valid=True
        for i in range(n):
            c=s[i]
            if(c=="("):
                stack.append(i)
            elif(c=="*"):
                stars.append(i)
            elif(c==")"):
                if(stack):
                    stack.pop()
                elif(stars):
                    stars.pop()
                else:
                    valid=False
                    break
        
        while stars and stack:
            c1=stars.pop()
            c2=stack.pop()
            if(c1<c2):
                #asterisk before (
                valid=False
                break
        if(stack or not valid):
            return False
        return True
        
                
                    
        
        
        