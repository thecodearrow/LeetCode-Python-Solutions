#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3361/
"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        if(node is None):
            return None
        if(node.val==val):
            return node
        if(val<node.val):
            return self.searchBST(node.left,val)
        else:
            return self.searchBST(node.right,val)