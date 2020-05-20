#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_valid(self,node,idx,sequence):
        if(node is None):
            #ran out of nodes 
            return False
        if(idx==len(sequence)-1):
            #last char in sequence
            if(node.left is not None or node.right is not None):
                #still nodes left to explore
                return False
            if(node.val!=sequence[idx]):
                #Value doesn't match!
                return False
            return True
        if(node.val!=sequence[idx]):
            return False
        p1=self.check_valid(node.left,idx+1,sequence)
        p2=self.check_valid(node.right,idx+1,sequence)
        return p1 or p2
        
        
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.check_valid(root,0,arr)
        
        