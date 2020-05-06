#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        jewels=set(J)
        for c in S:
            if(c in jewels):
                count+=1
                
        return count
        