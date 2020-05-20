#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

from collections import deque
class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        string=deque(s)
        for dir,amt in shift:
            if(dir==0):
                for i in range(amt):
                    char=string.popleft()
                    string.append(char)
            else:
                for i in range(amt):
                    char=string.pop()
                    string.appendleft(char)
                    
        ans="".join(string)
        return ans
        