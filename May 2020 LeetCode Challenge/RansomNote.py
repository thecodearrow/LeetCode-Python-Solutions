#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars=Counter(magazine)
        for r in ransomNote:
            if(r not in chars or chars[r]==0):
                return Falsex
            chars[r]-=1
        return True
        
        