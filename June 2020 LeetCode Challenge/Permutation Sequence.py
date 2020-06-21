"""
#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3366/

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

"""
class Solution:
    def next_permutate(self,a,n):
        idx=n-1
        while a[idx]<a[idx-1]:
            idx-=1
        #we have to find a place for a[idx-1]... that will be the smallest element greater than a[idx-1]
        min_idx=idx
        for j in range(idx,n):
            if(a[j]>a[idx-1]):
                min_idx=j
            else:
                break
        a[idx-1],a[min_idx]=a[min_idx],a[idx-1]
        #Now all numbers from i to n-1 are in descending order... sort them
        start=idx
        end=n-1
        while start<end:
            a[start],a[end]=a[end],a[start]
            start+=1
            end-=1
        return a
        
    def getPermutation(self, n: int, k: int) -> str:
        a=[i for i in range(1,n+1)]
        for i in range(1,k):
            a=self.next_permutate(a,n)
        
        a=[str(i) for i in a]
        return "".join(a)
        
        