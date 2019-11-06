#https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, string: str) -> str:
        len_string=len(string)
        if(len_string<=1):
            return string
    
        isPalindrome=[[0 for j in range(len_string)]for i in range(len_string)]
        paliI,paliJ=None,None
        for l in range(len_string):
            for i in range(len_string-l):
                p1=i
                p2=i+l
                if(string[p1]==string[p2]):
                    if(l<=1):
                        isPalindrome[p1][p2]=True
                        paliI,paliJ=p1,p2
                    elif(isPalindrome[p1+1][p2-1]):
                        isPalindrome[p1][p2]=True
                        paliI,paliJ=p1,p2
                    else:
                        isPalindrome[p1][p2]=False
        
        return string[paliI:paliJ+1]
            
        
        