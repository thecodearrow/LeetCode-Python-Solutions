#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructTree(self,preorder,start,end):
        if(start>end):
            return None
        root=TreeNode(preorder[start])
        if(start==end):
            return root
        right_exists=False
        for i in range(start,end+1):
            if(preorder[i]>preorder[start]):
                right_exists=True
                break
        if(not right_exists):
             root.left=self.constructTree(preorder,start+1,i)
             root.right=None
             return root
        root.left=self.constructTree(preorder,start+1,i-1)
        root.right=self.constructTree(preorder,i,end)
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.constructTree(preorder,0,len(preorder)-1)
        
        