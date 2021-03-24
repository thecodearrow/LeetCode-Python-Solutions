"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=[]
        carry=0
        i=len(a)-1
        j=len(b)-1
        len_a=len(a)
        len_b=len(b)
        while i>=0 or j>=0:
            if(i<0):
                digit_a=0
            else:
                digit_a=int(a[i])
            if(j<0):
                digit_b=0
            else:
                digit_b=int(b[j])
            digit_ans=(digit_a+digit_b+carry)%2
            carry=(digit_a+digit_b+carry)//2
            ans.append(str(digit_ans))
            i-=1
            j-=1
            
        if(carry==1):
            ans.append('1')
        return "".join(ans[::-1])