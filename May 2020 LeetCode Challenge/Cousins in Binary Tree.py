# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root,x,y):
        dist={root.val:0}
        parent={root.val:None}
        queue=[root]
        while queue:
            if(x in dist and y in dist):
                #explored both x and y 
                break
            node=queue.pop(0)
            if(node.left is not None):
                if(node.left.val not in dist):
                    #not visited left
                    dist[node.left.val]=dist[node.val]+1
                    parent[node.left.val]=node.val
                    queue.append(node.left)
            if(node.right is not None):
                if(node.right.val not in dist):
                    #not visited right
                    dist[node.right.val]=dist[node.val]+1
                    parent[node.right.val]=node.val
                    queue.append(node.right)
            
        if(parent[x]!=parent[y] and dist[x]==dist[y]):
            return True  
        return False
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        is_cousins=self.bfs(root,x,y)
        return is_cousins
        