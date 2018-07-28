#https://leetcode.com/problems/longest-palindromic-substring/description/

from collections import defaultdict
class Solution:
    def longestPalindrome(self, s):
      
        l=len(s)
        if(l<=1):
            return s
        
        isPali=defaultdict(lambda:False) #returns True if s[i:j] is a palindrome
        
        #Mark all length 1 palindromes
    
        maxLen=1 
        for i in range(l):
            isPali[(i,i)]=True
            paliI=i
            paliJ=i
            
        #Mark all length 2 palindromes 
        
        for i in range(l-1):
            if(s[i]==s[i+1]):
                maxLen=2
                isPali[(i,i+1)]=True 
                paliI=i
                paliJ=i+1
                
        
        #Mark all length >/3 palindromes
        
        for length in range(3,l+1):  #length starting from 3
            for i in range(0,l-length+1): #starting point
                j=i+length-1 #ending point
                #inner word will be from i+1 to j 
                if(s[i]==s[j] and isPali[(i+1,j-1)]):
                    isPali[(i,j)]=True 
                    if(length>maxLen):
                        maxLen=length
                        paliI=i 
                        paliJ=j 
                    
        return s[paliI:paliJ+1]
            
            
        
        