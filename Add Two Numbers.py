#https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def addTwoNumbers(self, l1, l2):
      
        a=[]
        b=[]
        current=l1
        while(current!=None):
            a.append(current.val)
            current=current.next
            
        current=l2
        while(current!=None):
            b.append(current.val)
            current=current.next
        
        a=a[::-1]
        b=b[::-1]
        
        l=len(a)
        if(len(b)>l):
            l=len(b)
        
        i=0
        num1=""
        num2=""
        for ele in a:
            num1+=str(ele)
        for ele in b:
            num2+=str(ele)
        
        num1=int(num1)
        num2=int(num2)
        ans=num1+num2
        ans_list=[]
        linkedlist=""
        for ele in str(ans):
            ans_list.append(int(ele))
        ans_list=ans_list[::-1]
       
        return ans_list