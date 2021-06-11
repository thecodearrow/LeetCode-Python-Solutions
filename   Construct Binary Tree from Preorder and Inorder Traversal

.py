#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3772/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findIdx(self,val):
        global find
        return find[val]
        return -1
        
    def traverse(self,l,r,n,preorder,inorder):
        
        if(l>r):
            return
        global pi
        rootVal=preorder[pi]
        pi+=1 #increment pi!
        rootNode=TreeNode(rootVal)
        idx=self.findIdx(rootVal)
        rootNode.left=self.traverse(l,idx-1,n,preorder,inorder)
        rootNode.right=self.traverse(idx+1,r,n,preorder,inorder)
        return rootNode
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n=len(preorder)
        global find,pi
        pi=0
        find={}
        for i in range(n):
            find[inorder[i]]=i
            
        return self.traverse(0,n-1,n,preorder,inorder)
        