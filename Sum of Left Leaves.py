# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        global left_sum
        left_sum=0
        def dfs(node,isLeft):
            if(node is None):
                return 
            if(node.left is None and node.right is None):
                #leaf node
                if(isLeft):
                    global left_sum
                    left_sum+=node.val
            dfs(node.left,True)
            dfs(node.right,False)
        
        dfs(root,False)
        return left_sum
