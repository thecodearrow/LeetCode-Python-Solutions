# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        global max_l
        max_l=0
        def dfs(node):
            if(node is None):
                return 0
            left_l=dfs(node.left)
            right_l=dfs(node.right)
            if(node.left and node.val!=node.left.val):
                #cut left path
                left_l=0
            if(node.right and node.val!=node.right.val):
                #cut right path
                right_l=0
            global max_l
            max_l=max(max_l,left_l+right_l)
            return 1+max(left_l,right_l)
        
        dfs(root)
        return max_l
