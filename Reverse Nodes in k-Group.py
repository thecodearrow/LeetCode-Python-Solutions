#https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lessThanKNodesLeft(self,head,k):
        current=head
        count=0
        while current:
            count+=1
            if(count==k):
                return False
            current=current.next
        
        return True
            
    def reverseKGroup(self, A: ListNode, k: int) -> ListNode:
        
        if(k==1):
            return A
        if(self.lessThanKNodesLeft(A,k)):
            #fewer than K nodes
            return A
        firstHead=None
        head,tail=None,None
        current=A
        while current:
            prev=None
            nextNode=None
            currentCopy=current
            if(self.lessThanKNodesLeft(currentCopy,k)):
                #do nothing! 
                tail.next=current
                return firstHead
            current=currentCopy
            for i in range(k):
                #normal reversing of a linkedlist
                nextNode=current.next
                current.next=prev
                prev=current
                current=nextNode
           
            head=prev
            if(firstHead is None):
                firstHead=head

            if(tail is not None):
                tail.next=head
            tail=currentCopy
        
        
       
        return firstHead
        
