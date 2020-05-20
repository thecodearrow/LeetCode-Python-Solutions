#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/

#Can be optimised further!

from collections import deque
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique_queue=deque()
        self.count={}
        for i,ele in enumerate(nums):
            self.add(ele)
            
    def showFirstUnique(self) -> int:
        while(self.unique_queue and self.count[self.unique_queue[0]]!=1):
            self.unique_queue.popleft()
        if(self.unique_queue):
            return self.unique_queue[0]
        return -1
            
        
    def add(self, value: int) -> None:
        if(value in self.count):
            self.count[value]+=1
        else:
            self.count[value]=1
            self.unique_queue.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)