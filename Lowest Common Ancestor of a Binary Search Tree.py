#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None):
            return None
        node=root
        while node:
            if(p.val>node.val and q.val>node.val):
                node=node.right
            elif(p.val<node.val and q.val<node.val):
                node=node.left
            else:
                return node
                
        
        