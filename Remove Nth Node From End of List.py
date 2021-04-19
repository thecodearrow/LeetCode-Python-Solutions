#https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3712/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #We add a dummy node to handle edge cases (like removal of the first node!)
        dummy=ListNode(0)
        dummy.next=head
        first,second=dummy,dummy
        for i in range(n+1):
            #since we added one node
            second=second.next
        
        while second:
            first=first.next
            second=second.next
        
        first.next=first.next.next
        return dummy.next