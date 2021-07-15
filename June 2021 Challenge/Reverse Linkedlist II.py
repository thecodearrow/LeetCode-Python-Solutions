#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3789/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self,head,left,right):
        if(head is None or head.next is None):
            #0 or 1 nodes!
            return head
        #startNode, endNode, startNodePrev, endNodeNex
        current=head
        for i in range(left-2):
            current=current.next
        
        if(left==1):
            #edge case! 
            startNode=head
            startNodePrev=None
        else:
            startNodePrev=current
            startNode=current.next
        
        
        #Normal reversing of a linkedlist
        prev=None
        current=startNode
        for i in range(right-left+1):
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
            
        endNode=prev
        endNodeNext=current
        startNode.next=endNodeNext 
        if(startNodePrev is None):
            return endNode
        
        startNodePrev.next=endNode
        return head