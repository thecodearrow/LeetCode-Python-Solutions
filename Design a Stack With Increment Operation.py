class Node:
    def __init__(self,val):
        self.val=val
        self.inc=0
class CustomStack:
    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxSize=maxSize

    def push(self, x: int) -> None:
        currentSize=len(self.stack)
        if(currentSize==self.maxSize):
            return 
        node=Node(x) #(val,inc=0)
        self.stack.append(node)
        

    def pop(self) -> int:
        if(not self.stack):
            return -1
        poppedNode=self.stack.pop()
        ele,inc=poppedNode.val,poppedNode.inc
        if(self.stack):
            #pass down inc to the rest of the elements! 
            self.stack[-1].inc+=inc 
        actualEle=ele+inc
        return actualEle
        

    def increment(self, k: int, val: int) -> None:
        idx=min(len(self.stack)-1,k-1)
        if(self.stack):
            #increment idx node by val
            self.stack[idx].inc+=val
            
     


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
