"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        diameter=0
        def dfs(node):
            if(node is None):
                return 0
            max_l=0
            second_max_l=0
            for c in node.children:
                l=dfs(c)
                if(l>max_l):
                    second_max_l=max_l #update second max l to current max l (IMP!)
                    max_l=l
                elif(l>second_max_l):
                    second_max_l=l
            
            nonlocal diameter
            diameter=max(diameter,max_l+second_max_l) #diameter passing through current node
            return 1+max_l
        dfs(root)
        return diameter
