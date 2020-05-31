#https://leetcode.com/problems/reverse-pairs/submissions/

"""
Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j]. 
Return the number of important reverse pairs in the given array A. 

"""
class Solution:
    def calculateSplitCount(self,l,r):
        #count split count here! (VERY IMP!)
        i=0
        j=0
        split_count=0
        m=len(l)
        n=len(r)
        while i<m and j<n:
            if(l[i]<=2*r[j]):
                i+=1
            else:
                split_count+=(m-i)
                j+=1
        return split_count
    def impPairsCount(self,array,start,end):
        if(start>=end):
            return array[start:end+1],0
        mid=(start+end)//2
        l,left_count=self.impPairsCount(array,start,mid)
        r,right_count=self.impPairsCount(array,mid+1,end)
        split_count=self.calculateSplitCount(l,r)
        array=self.merge(l,r)
        imp_pairs_count=left_count+right_count+split_count
        return array,imp_pairs_count
        
    def merge(self,l,r):
        m=len(l)
        n=len(r)
        i=0
        j=0
        merged=[]
        while i<m and j<n:
            if(l[i]<=r[j]):
                merged.append(l[i])
                i+=1
            else:
                merged.append(r[j])
                j+=1
        while i<m:
            merged.append(l[i])
            i+=1
            
            
        while j<n:
            merged.append(r[j])
            j+=1
    
        return merged
    def reversePairs(self, nums: List[int]) -> int:
        array,imp_pairs_count=self.impPairsCount(nums,0,len(nums)-1)
        return imp_pairs_count