class RandomizedCollection:
    def __init__(self):
        self.elements=[]
        self.mapping=defaultdict(set) #ele -> {idx1,idx2}
        self.size=0
    def insert(self, val: int) -> bool:
        idx=len(self.elements)
        self.elements.append(val) #add val to list
        self.mapping[val].add(idx) #add idx to ele set
        if(len(self.mapping[val])>1):
            #already present
            return False
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.mapping or len(self.mapping[val])==0):
            #element not present
            return False
        self.moveToEndRemove(val) #IMP, move val to end of elements! 
        return True
    def moveToEndRemove(self,currEle):
        #move element to the end, swap current last element, remove from list and update mapping
        lastEle,lastIdx=self.elements[-1],len(self.elements)-1
        if(lastEle==currEle):
            #same as the last element! 
            self.mapping[lastEle].remove(lastIdx)
            self.elements.pop() #pop off the element from end
        else:
            currIdx=self.mapping[currEle].pop()
            self.elements[currIdx],self.elements[lastIdx]=self.elements[lastIdx], self.elements[currIdx] #move to end! 
            self.elements.pop() #pop off the element from end
            #update mapping! 
            self.mapping[lastEle].remove(lastIdx)
            self.mapping[lastEle].add(currIdx)
      

    def getRandom(self) -> int:
        return random.choice(self.elements)
        # idx=random.randint(0,self.size-1)
        # return self.elements[idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
