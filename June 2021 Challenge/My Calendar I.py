#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3774/

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class MyCalendar:

    def __init__(self):
        self.times=[]
        self.count=0
        self.rootNode=None
    
    def isOverlap(self,time1,time2):
        #no overlap has just two cases!
        s1,e1=time1
        s2,e2=time2
        if(e1<=s2):
            #(s1,e1) comes before (s2,e2)...so no overlap
            return False
        if(s1>=e2):
            #(s1,e1) comes after (s2,e2)... so no overlap
            return False
        return True #there's a overlap
        
    
    def addTime(self,current_time):
        self.times.append(current_time)
        self.count+=1
    
    def handleBooking(self,current_time):
        start,end=current_time
        for time in self.times:
            if(self.isOverlap(time,current_time)):
                return False
        
        self.addTime(current_time)
        return True
            
    
    def insertIntoTree(self,node,current_time):
        if(node is None):
            if(self.rootNode is None):
                self.rootNode=TreeNode(current_time)
            return True
        else:
            s,e=current_time
            nodeStart,nodeEnd=node.val
            if(e<=nodeStart):
                #goLeft
                if(node.left is None):
                    node.left=TreeNode(current_time)
                    return True
                else:
                    return self.insertIntoTree(node.left,current_time)
            
            elif(s>=nodeEnd):
                #go right
                if(node.right is None):
                    node.right=TreeNode(current_time)
                    return True
                else:
                    return self.insertIntoTree(node.right,current_time)
                
            else:
                #can't be inserted anywhere! 
                return False
            
        
        
    def book(self, start: int, end: int) -> bool:
        current_time=(start,end)
        #return self.handleBooking(current_time)  #using an array! 
        
        #using a tree
        return self.insertIntoTree(self.rootNode,current_time)
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)