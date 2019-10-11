#https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
from collections import defaultdict
class Solution(object):
    def longestSubsequence(self, arr, difference):
        current_max=0
        lis=defaultdict(lambda:1) #lis ending at ele
        present=defaultdict(lambda:False)
        for i in range(len(arr)):
            ele=arr[i]
            if(present[ele-difference]):
                lis[ele]=lis[ele-difference]+1
            present[ele]=True
            current_max=max(current_max,lis[ele])
        
        return current_max
                
        