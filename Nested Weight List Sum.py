# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def usingBFS(self,nestedList):
        queue=deque(nestedList)
        ans=0
        d=1
        while queue:
            n=len(queue)
            for i in range(n):
                current=queue.pop()
                if(current.isInteger()):
                    number=current.getInteger()
                    ans+=(number*d)
                else:
                    #add it to the front
                    #sort of like creating a new queue! 
                    current_list=current.getList()
                    for arr in current_list:
                        queue.appendleft(arr)
            d+=1 #increase depth for the next queue
            
            
        return ans
    def depthSum(self, nestedList: List[NestedInteger]) -> int:    
        
        #return self.usingBFS(nestedList)
        global ans
        ans=0 #sum
        def dfs(arr,d):
            for a in arr: 
                if(a.isInteger()):
                    #isInteger
                    global ans
                    number=a.getInteger()
                    ans+=(number*d)
                else:
                    #is nested list
                    dfs(a.getList(),d+1)
        dfs(nestedList,1)
        return ans
