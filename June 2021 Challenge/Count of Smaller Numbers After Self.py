#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3792/

from sortedcontainers import SortedList
class FenwickTree:
    def __init__(self):
        self.offset=10**4
        self.MAX=2*self.offset+1
        self.fenwick_arr=[0]*(self.MAX+1) #1-indexed!
        
    def add(self,index,val):
        index+=1 #0-index to 1-inde
        index+=self.offset #due to negative values! 
        while index<=self.MAX:
            self.fenwick_arr[index]+=val
            index+=(index & -index)
           
    def getCount(self,index):
        #assuming it's 1-index
        count=0
        index+=self.offset #due to negative values! 
        while index!=0:
            count+=self.fenwick_arr[index]
            index-=(index & -index)
        
        return count
class Solution:
    def solnUsingSortedList(self,nums):
        #using sortedlist! 
        elements=SortedList()
        ans=[]
        for ele in reversed(nums):
            idx=elements.bisect_left(ele)
            ans.append(idx)
            elements.add(ele)
        
        return ans[::-1]
    def countSmaller(self, nums: List[int]) -> List[int]:
        #return solnUsingSortedList(nums)
        ans=[]
        fw=FenwickTree()
        for ele in reversed(nums):
            c=fw.getCount(ele)
            ans.append(c)
            fw.add(ele,1) #marking the element by 1
        print(fw.fenwick_arr)
        return ans[::-1]
    
    
        
        