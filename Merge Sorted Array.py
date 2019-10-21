#https://leetcode.com/problems/merge-sorted-array/submissions/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n=len(nums1)
        l2=len(nums2)
        if(n==0):
            return
        if(l2==0):
            return
        p1=n-l2-1
        p2=l2-1
        currentIndex=n-1
        while p1>=0 and p2>=0:
            if(nums1[p1]>=nums2[p2]):
                nums1[currentIndex]=nums1[p1]
                p1-=1
                currentIndex-=1
            else:
                nums1[currentIndex]=nums2[p2]
                p2-=1
                currentIndex-=1
                
                
        while p2>=0:
            #left over elements
            nums1[currentIndex]=nums2[p2]
            p2-=1
            currentIndex-=1
                
        
                
        