#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hare=head
        turtle=head
        while hare.next!=None:
            turtle=turtle.next
            hare=hare.next
            if(hare.next!=None):  
                hare=hare.next
        
        return turtle
        
        