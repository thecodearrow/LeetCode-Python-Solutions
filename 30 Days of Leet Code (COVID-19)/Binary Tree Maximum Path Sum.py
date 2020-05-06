#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3314/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.maxVSum=-float("inf")
    def maxDFS(self,node):
        if(node is None):
            return 0
        left_gain=max(self.maxDFS(node.left),0) #0 because negative branches can be ignored!
        right_gain=max(self.maxDFS(node.right),0)
        
        #left,root,right V structure gains! (calculated separately using global variable) 
        currentVSum=left_gain+node.val+right_gain
        self.maxVSum=max(self.maxVSum,currentVSum)
        
        net_gain=node.val+max(left_gain,right_gain)
        return net_gain
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxDFS(root)
        return self.maxVSum
        
        