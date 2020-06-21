#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3347/

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if(root is None):
            return
        queue=[root]
        while queue:
            node=queue.pop()
            node.left,node.right=node.right,node.left
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        
        return root
            
    def invertTreeRecursive(self, node: TreeNode) -> TreeNode:
        if(node is None):
            return
        leftChild=self.invertTree(node.left)
        rightChild=self.invertTree(node.right)
        node.left=rightChild
        node.right=leftChild
        return node