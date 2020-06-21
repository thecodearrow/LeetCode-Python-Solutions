#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3358/

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.containerMap={}
        self.containerList=[]
        self.size=0
        
        
    def swapToEndAndDelete(self,val):
        #swap to end and delete
        #update index for the swapped element
        #delete the last element and update size
        currIdx=self.containerMap[val]
        self.containerList[currIdx], self.containerList[-1]= self.containerList[-1], self.containerList[currIdx]
        self.containerMap[self.containerList[currIdx]]=currIdx 
        del self.containerMap[val]
        self.containerList.pop()
        self.size-=1
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(val in self.containerMap):
            return False
        else:
            self.containerMap[val]=self.size #current index
            self.containerList.append(val)
            self.size+=1
            return True

    
        
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if(val in self.containerMap):
            self.swapToEndAndDelete(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        if(self.size>0):
            random_idx=random.randint(0,self.size-1)
            return self.containerList[random_idx]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()