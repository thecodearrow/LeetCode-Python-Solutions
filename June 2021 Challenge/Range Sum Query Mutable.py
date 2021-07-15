#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3783/


#can be solved using a fenwick tree!

class NumArray:

    def __init__(self, nums):
        self.size=len(nums)
        self.fenwick_arr=[0]*(self.size+1) #1-indexed!
        self.arr=[0]+nums[:]
        for i,ele in enumerate(nums):
            self.add(i,ele)
    
    def add(self, index: int, val: int) -> None:
        index+=1 #0-index to 1-inde
        while index<=self.size:
            print(index,)
            self.fenwick_arr[index]+=val
            index+=(index & -index)
    def update(self, index: int, val: int) -> None:
        index+=1 #0-index to 1-index
        diff=val-self.arr[index] #how much to update! 
        self.arr[index]=val
        while index<=self.size:
            self.fenwick_arr[index]+=diff
            index+=(index & -index)
        
           
    def getSum(self,index):
        #assuming it's 1-index
        current_sum=0
        while index!=0:
            current_sum+=self.fenwick_arr[index]
            index-=(index & -index)
        
        return current_sum

    def sumRange(self, left: int, right: int) -> int:
        left+=1
        right+=1  #0-index to 1-index
        return self.getSum(right)-self.getSum(left-1)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

obj = NumArray([1,2,3,4,5,6,7,8])
print(obj.fenwick_arr)