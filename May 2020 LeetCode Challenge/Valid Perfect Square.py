"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start=1
        end=num
        while start<=end:
            mid=start+(end-start)//2
            square=mid*mid
            if(square==num):
                return True
            elif(square<num):
                start=mid+1
            else:
                end=mid-1
            
        return False
        