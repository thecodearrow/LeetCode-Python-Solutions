# Definition for a binary tree node.
#https://leetcode.com/problems/diameter-of-binary-tree

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#O(n) solution! 
#The diameter need not pass throught the root

class Solution:
    def getHeight(self,node):
        if(node is None):
            return 0
        left_height=self.getHeight(node.left)
        right_height=self.getHeight(node.right)
        global diameter
        diameter=max(diameter,left_height+right_height)
        return 1+max(left_height,right_height)
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        global diameter
        diameter=0
        self.getHeight(root)
        return diameter
    
        