#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def height(self,root):
        if(root is None):
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    
    def diameterOfBinaryTree(self, root):
        if(root is None):
            return 0
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        diameter=max(lheight+rheight,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return diameter
        
        
        
        
        
        
        
        