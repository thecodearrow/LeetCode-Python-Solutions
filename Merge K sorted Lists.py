#https://leetcode.com/problems/merge-k-sorted-lists/solution/

#O(N*K solution similar to the merge sort procedure!)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        newList=ListNode(None)
        headNewList=newList
        k=len(lists)
        if(k==0):
            return None
        while True:
            min_element=float("inf")
            min_list_index=None
            for i in range(k):
                currentNode=lists[i]
                if(currentNode!=None):
                    if(currentNode.val<min_element):
                        min_element=currentNode.val
                        min_list_index=i
            if(min_list_index!=None):
                newNode=ListNode(min_element)
                newList.next=newNode
                newList=newList.next
                lists[min_list_index]=lists[min_list_index].next
            else:
                break
                
        return headNewList.next
            
            
            
#https://leetcode.com/problems/merge-k-sorted-lists/solution/

#Using Priority Queue (Min-Heap)
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        newList=ListNode(None)
        headNewList=newList
        k=len(lists)
        if(k==0):
            return None
        n=lists[0]
        heap=[]
        heapq.heapify(heap)
        for index,node in enumerate(lists):
            if(node):
                heapq.heappush(heap,[node.val,index])
        
        while heap:
            minNodeValue,minNodeIndex=heapq.heappop(heap)
            newNode=ListNode(minNodeValue)
            newList.next=newNode
            newList=newList.next
            if(lists[minNodeIndex].next):
                #Add the next node to heap
                lists[minNodeIndex]=lists[minNodeIndex].next
                heapq.heappush(heap,[lists[minNodeIndex].val,minNodeIndex])
                
        return headNewList.next
            
            
            
        