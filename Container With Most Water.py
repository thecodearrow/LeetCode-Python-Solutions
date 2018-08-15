#https://leetcode.com/problems/container-with-most-water/description/

#Two Pointer approach!


class Solution:
    def maxArea(self, height):
        
        n=len(height)
        maxi=-10**9
        start=0
        end=n-1
        while start<end:
            if(height[start]<height[end]):
                a=(end-start)*height[start]
                start+=1
            else:
                a=(end-start)*height[end]
                end-=1
            maxi=max(maxi,a)

        return maxi