#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minStack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if(self.stack):
            min_element=min(x,self.minStack[-1])
        else:
            min_element=x
        self.stack.append(x)
        self.minStack.append(min_element)
        
        

    def pop(self):
        """
        :rtype: None
        """
        if(self.stack):
            self.stack.pop()
            self.minStack.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()