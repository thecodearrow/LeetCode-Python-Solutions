#https://leetcode.com/problems/backspace-string-compare/

#Using Extra Space
class Solution(object):
    def backspaceCompare(self, S, T):
        stack1=[""]
        stack2=[""]
        index=0
        l1=len(S)
        l2=len(T)
        while index<l1 or index<l2:
            if(index<l1):
                c1=S[index]
                if(c1=="#"):
                    if(stack1[-1]!=""):
                        stack1.pop()
                else:
                    stack1.append(c1)
            if(index<l2):
                c2=T[index]
                if(c2=="#"):
                    if(stack2[-1]!=""):
                        stack2.pop()
                else:
                    stack2.append(c2)
                
            index+=1
        index=0
        while stack1 and stack2:
            c1=stack1.pop()
            c2=stack2.pop()
            if(c1!=c2):
                return False
            
            
        
        return True

#Without using Extra space
        