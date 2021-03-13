#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3669/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        substrings=set()
        for i in range(n-k+1):
            substr=s[i:i+k]
            substrings.add(substr)
        print(substrings)
        return True if len(substrings)==2**k else False #basically if it contains all possible substrings of length k

        
        
        