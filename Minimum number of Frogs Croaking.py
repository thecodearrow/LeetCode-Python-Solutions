#https://leetcode.com/contest/weekly-contest-185/problems/minimum-number-of-frogs-croaking/

from collections import defaultdict
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        croak=["c","r","o","a","k"]
        count=defaultdict(lambda:0)
        #check if letters are out of order
        for c in croakOfFrogs:
            count[c]+=1
            for frog_char in croak:
                if(c==frog_char):
                    break
                if(count[c]>count[frog_char]):
                    return -1
        count=0
        frogs=0
        for c in croakOfFrogs:
            if(c=="c"):
                count+=1
            elif(c=="k"):
                count-=1
            frogs=max(frogs,count)
        
        if(count!=0):
            return -1
        return frogs
                
            
        
        
        
        