#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3660/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Solution a Based on the difference between the lists! 
class Solution:
    def findLength(self,head):
        current=head
        length=0
        while current:
            length+=1
            current=current.next
        return length
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA=self.findLength(headA)
        lenB=self.findLength(headB)
        if(lenB<lenA):
            lenA,lenB=lenB,lenA
            headA,headB=headB,headA
        
        d=lenB-lenA
        currA=headA
        currB=headB
        for i in range(d):
            currB=currB.next
        
        while currA and currB:
            if(currA==currB):
                return currA
            currA=currA.next
            currB=currB.next



#A clever solution based on the fact that a+s+b = b+s+a 


class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
       
        currA=headA
        currB=headB
        
        while currA!=currB:
            currA=currA.next if currA else headB
            currB=currB.next if currB else headA
        
        return currA
            
            