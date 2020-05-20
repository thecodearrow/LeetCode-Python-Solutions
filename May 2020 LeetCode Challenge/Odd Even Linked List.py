#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331/

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return head
        odd_head=head
        even_head=head.next
        currentNode=head
        while currentNode!=None and currentNode.next!=None:
            oddNode=currentNode
            evenNode=currentNode.next
            oddNode.next=oddNode.next.next #remove the link to the even node
            if(evenNode.next!=None):
                evenNode.next=evenNode.next.next
            if(currentNode.next!=None):
                currentNode=currentNode.next #the pointer used to traverse the linkedlist
            
        currentNode.next=even_head
        return odd_head