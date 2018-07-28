#Uses Binary Search to solve it in O(log(min(m,n)))

#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

#MINDBLOWING EXPLAINATION https://www.youtube.com/watch?v=LPFhl65R7ww 

import sys
class Solution:
    
    def findMedian(x1,y1,x2,y2,size):
    
        if(size%2==0):
            left_part=max(x1,y1)
            right_part=min(x2,y2)
            return (left_part+right_part)/2
        else:
            return min(x2,y2)

    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)

        #ensure ALWAYS nums1 is the smaller array of the two! If noy, swap
        if(m>n):
            nums1,nums2=nums2,nums1
            m,n=n,m 

        low=0
        high=m
        while low<=high:
            cutX=(low+high)//2
            cutY=((m+n)//2)-cutX
            #handle edge cases
            x1=(-1*sys.maxsize) if cutX==0 else nums1[cutX-1]
            x2=(sys.maxsize) if cutX==m else nums1[cutX]
            y1=(-1*sys.maxsize) if cutY==0 else nums2[cutY-1]
            y2=(sys.maxsize) if cutY==n else nums2[cutY]
            if(x1<=y2 and y1<=x2):
                ans=Solution.findMedian(x1,y1,x2,y2,m+n)
                break
            elif(x1>y2):
                high=cutX-1
            else:
                low=cutX+1

        return(ans)






