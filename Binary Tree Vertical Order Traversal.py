# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return []
        #because bfs goes level wise, it prevents the need for sorting
        queue=deque([(root,0)])
        cols=defaultdict(list)
        max_c=-float("inf")
        min_c=float("inf")
        while queue:
            node,c=queue.popleft()
            cols[c].append(node.val)
            max_c=max(max_c,c)
            min_c=min(min_c,c)
            if(node.left):
                queue.append((node.left,c-1))
            if(node.right):
                queue.append((node.right,c+1))
                
        
        return [cols[c] for  c in range(min_c,max_c+1)]
