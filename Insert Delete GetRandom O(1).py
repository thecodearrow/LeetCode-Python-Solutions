import random
class RandomizedSet:
    def __init__(self):
        self.elements=[]
        self.mapping={} #ele -> idx
        self.size=0
    def insert(self, val: int) -> bool:
        if(val in self.mapping):
            #already present
            return False
        idx=self.size
        self.elements.append(val) #add val to list
        self.mapping[val]=idx #create mapping
        self.size+=1 #increment size
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.mapping):
            #element not present
            return False
        self.moveToEndAndRemove(val) #IMP, move val to end of elements! 
        return True
    def moveToEndAndRemove(self,currEle):
        currIdx=self.mapping[currEle]
        lastEle=self.elements[-1]
        lastIdx=self.size-1
        if(currIdx==lastIdx):
            self.elements.pop()
            del self.mapping[currEle]
        else:
            #swap element with the last element, pop off element from end and update mapping
            self.elements[currIdx],self.elements[lastIdx]=self.elements[lastIdx],self.elements[currIdx]
            #pop off val from end! 
            self.elements.pop()
            del self.mapping[currEle] #remove mapping of currEle
            self.mapping[lastEle]=currIdx #update mapping 
        self.size-=1  #decrement size

    def getRandom(self) -> int:
        #return random.choice(self.elements)
        idx=random.randint(0,self.size-1)
        return self.elements[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
