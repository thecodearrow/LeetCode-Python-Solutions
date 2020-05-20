#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/

"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
"""
class Solution:
    def checkInclusion(self, small: str, big: str) -> bool:
        char_count=[0]*26
        for c in small:
            char_index=ord(c)-ord('a')
            char_count[char_index]+=1
        
        i=0
        j=0
        ls=len(small)
        lb=len(big)
        while j<lb:
            c=big[j]
            char_index=ord(c)-ord('a')
            if(char_count[char_index]>0):
                char_count[char_index]-=1
                j+=1
                if(j-i==ls):
                    return True
            elif(i==j):
                i+=1
                j+=1
            elif(char_count[char_index]<=0):
                char_index=ord(big[i])-ord('a')
                char_count[char_index]+=1
                i+=1
        
        return False
                
                