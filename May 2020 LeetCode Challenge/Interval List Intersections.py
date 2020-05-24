"""
#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
"""
class Solution:
    def isOverlap(self,s1,e1,s2,e2):
        if(s2<=s1 and s1<=e2):
            #s1 lies between [s2,e2] i.e. right overlap
            return True
        if(s2<=e1 and e1<=e2):
            #e1 lies between [s2,e2] i.e. left overlap
            return True
        return True
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        intersections=[]
        n1=len(A)
        n2=len(B)
        while i<len(A) and j<len(B):
            s1,e1=A[i]
            s2,e2=B[j]
            interval_start=max(s1,s2)
            interval_end=min(e1,e2)
            if(interval_start<=interval_end):
                intersections.append([interval_start,interval_end])
        
            if(e1<=e2):
                i+=1
            else:
                j+=1
            
        return intersections
        