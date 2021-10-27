# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        global moves
        moves=0
        def minMoves(node):
            if(node is None):
                return 0
            lc=minMoves(node.left)
            rc=minMoves(node.right)
            global moves
            moves+=abs(lc)+abs(rc)+(node.val-1)
            return lc+rc+(node.val-1) #excess coins
            
        minMoves(root)
        return moves
