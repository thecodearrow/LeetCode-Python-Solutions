#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1=head
        p2=head
        
        #advance p2 to reach the kth node
        for i in range(k-1):
            p2=p2.next
        
        
        startK=p2
        p2=p2.next #advance p2
        
        #find endK
        while p2:
            p1=p1.next
            p2=p2.next
        
        
        endK=p1 #wherever p1 stopped when p2 reached the end!
        startK.val,endK.val=endK.val,startK.val
        return head
        
        
        
            
        
        
        
        
        