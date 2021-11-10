# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if(node is None):
                return -float("inf"),float("inf"),True,0
            left_max,left_min,left_valid,left_size=dfs(node.left)
            right_max,right_min,right_valid,right_size=dfs(node.right)
            current_size=left_size+right_size+1
            current_valid=False
            if(left_valid and right_valid and node.val>left_max and node.val<right_min):
                #valid bst
                global ans 
                ans=max(ans,current_size)
                current_valid=True
            current_max=max(right_max,node.val)
            current_min=min(left_min,node.val)
            return current_max,current_min,current_valid,current_size
        global ans
        ans=0 #largest size
        dfs(root)
        return ans
