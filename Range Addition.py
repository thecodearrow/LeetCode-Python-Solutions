class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        cum=[0]*(length+1) #cumulative array
        for l,r,val in updates:
            cum[l]+=val #add at l
            cum[r+1]-=val #subtract at r+1
        
        #one final step
        for i in range(1,length):
            cum[i]+=cum[i-1]
        cum.pop() #pop off the extra element
        return cum
            
