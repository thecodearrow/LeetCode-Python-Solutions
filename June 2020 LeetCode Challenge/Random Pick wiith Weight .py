"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

"""
import random
class Solution:

    def __init__(self, w: List[int]):
        self.cum_freq=[w[0]]
        for i in range(1,len(w)):
            self.cum_freq.append(self.cum_freq[i-1]+w[i])
        
        

    def pickIndex(self) -> int:
        random_number=random.randint(1,self.cum_freq[-1])
        #This can be optimised using Binary Search! 
        start=0
        end=len(self.cum_freq)-1
        to_return_index=len(self.cum_freq)-1
        while start<=end:
            mid=(start+end)//2
            if(random_number<=self.cum_freq[mid]):
                to_return_index=min(to_return_index,mid)
                end=mid-1
            else:
                start=mid+1
        return to_return_index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()