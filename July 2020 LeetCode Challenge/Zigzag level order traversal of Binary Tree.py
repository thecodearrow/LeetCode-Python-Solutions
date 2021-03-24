

"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3398/

Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from collections import defaultdict,deque
class Solution:
    def zigzagLevelOrder(self, root):
        levels=defaultdict(list)
        queue=deque([(root,0)])
        while queue:
            node,level=queue.popleft()
            if(node is not None):
                levels[level].append(node.val)
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))
            
        ans=[]
        for i in range(len(levels)):
            if(i%2==0):
                ans.append(levels[i][:])
            else:
                ans.append(levels[i][::-1])
        
        return ans
                
            