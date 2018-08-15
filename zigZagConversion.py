#https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s, numRows):
       
        
        n=numRows
        if(n==1): #edge case
            return s
        pattern=[]
        for i in range(n):
            pattern.append([])
        current=0    
        moveDown=True
        for c in s:
            pattern[current].append(c)
            if(current==0):
                moveDown=True 
            elif(current==n-1):
                moveDown=False
            
            if(moveDown):
                current+=1
            else:
                current-=1
            
            
        ans=""    
        for p in pattern:
            for c in p:
                ans+=c
            
        return ans
            
            
            
            
        