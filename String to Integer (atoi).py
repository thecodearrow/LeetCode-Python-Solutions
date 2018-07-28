#https://leetcode.com/problems/string-to-integer-atoi/description/

#STUPID PROBLEM 

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str=str.strip()
        number=""
        nums=set(['0','1','2','3','4','5','6','7','8','9'])
        neg=100 #sign not set
        digits_seen=False
        for s in str:
            if(s=="-" and neg==100 and not digits_seen):
                neg=True
            elif(s=="+" and neg==100 and not digits_seen):
                neg=False
            elif(s=="."):
                break
            elif(s not in nums):
                break
            else:
                number+=s
                digits_seen=True
        if(number==""):
            number="0"
        number=int(number)          
        if(neg==True):
            number=-1*number
        imax=2**31-1
        imin=-1 * 2**31

        if(number<imin):
            return imin
        elif number>imax:
            return imax
        else:
            return number
        