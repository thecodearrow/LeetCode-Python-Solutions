#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Use a stack to remove digits
        ans=[]
        l=len(num)
        skipped=0
        stack=[]
        for i in range(l):
            ele=num[i]
            while stack and skipped<k and stack[-1]>ele:
                skipped+=1
                stack.pop()
            stack.append(ele)
         
        #If we can still remove digits, start removing from the end
        while stack and skipped<k:
            stack.pop()
            skipped+=1
        
        #Also check for empty list and leading zeros
        start=0
        for ele in stack:
            if(ele!='0'):
                break
            start+=1
        
        ans="".join(stack[start:])
        if(ans==""):
            return '0'
        return ans
        
        
        
        
       
        
        
        
        
        
        