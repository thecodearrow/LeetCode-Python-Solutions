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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        #(maxDepth+1)*sumOf(ele) - sumOf(d*ele)
        #(maxDepth+1)*normalSum - weightedSum
        global normalSum
        global weightedSum
        global max_d
        normalSum=0
        weightedSum=0
        max_d=0
        def dfs(arr,d):
            global max_d
            max_d=max(max_d,d)
            for a in arr: 
                if(a.isInteger()):
                    #isInteger
                    global normalSum,weightedSum
                    number=a.getInteger()
                    normalSum+=number
                    weightedSum+=(number*d)
                else:
                    #is nested list
                    dfs(a.getList(),d+1)
        
        dfs(nestedList,1)
        ans=(max_d+1)*normalSum - weightedSum
        return ans
