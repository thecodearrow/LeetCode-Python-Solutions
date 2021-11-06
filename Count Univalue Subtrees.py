# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        def dfs(node):
            if(node is None):
                return True
            isLeftUni=dfs(node.left)
            isRightUni=dfs(node.right)
            left_val=node.left.val if node.left else None
            right_val=node.right.val if node.right else None
            if(isLeftUni and isRightUni):
                global ans
                uni_status=False #univalue
                if(left_val==right_val==None):
                    #leaf node
                    uni_status=True
                elif(left_val is None and right_val==node.val):
                    uni_status=True
                elif(right_val is None and left_val==node.val):
                    uni_status=True
                elif(node.val==left_val==right_val):
                    uni_status=True
                    
                if(uni_status):
                    ans+=1 #increment count
                    return True
            return False
        dfs(root)
        return ans
