# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinelNode=ListNode(0) #dummyNode
        sentinelNode.next=head
        current=sentinelNode
        while current:
            if(current.next and current.next.next and (current.next.val==current.next.next.val)):
                duplicateVal=current.next.val
                nonDuplicateNode=current.next
                while nonDuplicateNode and nonDuplicateNode.val==duplicateVal:
                    nonDuplicateNode=nonDuplicateNode.next
                current.next=nonDuplicateNode
            else:
                current=current.next
        
        
        return sentinelNode.next
        
