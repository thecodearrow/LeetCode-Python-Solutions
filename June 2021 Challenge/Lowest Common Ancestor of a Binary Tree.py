# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None):
            return 
        if(root==p or root==q):
            return root
        leftChild=self.lowestCommonAncestor(root.left,p,q)
        rightChild=self.lowestCommonAncestor(root.right,p,q)
        if(leftChild and rightChild):
            return root
        return leftChild if leftChild else rightChild
       