#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3375/
class Solution:
    def numWays(self,i,j,n,m,cache):
        if(i==n):
            return 0
        if(j==m):
            return 0
        key=(i,j)
        if(key in cache):
            return cache[key]
        if(i==n-1 and j==m-1):
            return 1
        cache[key]=self.numWays(i+1,j,n,m,cache)+self.numWays(i,j+1,n,m,cache)
        return cache[key]
    def uniquePaths(self, m: int, n: int) -> int:
        return self.numWays(0,0,n,m,{})
        