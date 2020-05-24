#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3335/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,node,params):
        if(node is None):
            return
        if(count==0):
            #ans has been found
            return
        ans=self.inorder(node.left,params)
        params["count"]-=1
        if(params["count"]==0):
            params["ans"]=node.val
            return
        self.inorder(node.right,params)
        
        
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        params={"count":k,"ans":None}
        self.inorder(root,params)
        return params["ans"]
        