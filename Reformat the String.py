#https://leetcode.com/contest/weekly-contest-185/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        char=[]
        digits=[]
        nums=set(['0','1','2','3','4','5','6','7','8','9'])
        l=len(s)
        if(l==1):
            return s
        
        for c in s:
            if(c in nums):
                digits.append(c)
            else:
                char.append(c)
        output=[]
        l1=len(char)
        l2=len(digits)
        
        for i in range(min(l1,l2)):
            c1=char.pop()
            c2=digits.pop()
            if(l1>l2):
                output.append(c1)
                output.append(c2)
            else:
                output.append(c2)
                output.append(c1)
        valid=True
        if(l1>l2):
            if(len(char)==1):
                output.append(char.pop())
            else:
                valid=False
        elif(l2>l1):
            if(len(digits)==1):
                output.append(digits.pop())
            else:
                valid=False
        
        if(len(digits)!=0 or len(char)!=0):
            valid=False
        
        if(valid):
            return "".join(output)
        return ""
            
            
            
            