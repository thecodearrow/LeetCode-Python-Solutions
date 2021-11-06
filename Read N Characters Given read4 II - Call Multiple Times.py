# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue=deque()
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
        #use a QUEUE to keep track of those extra reads! 
        buf4=['0']*4
        chars_read=0
        while chars_read<n :
            if(self.queue):
                buf[chars_read]=self.queue.popleft()
                chars_read+=1
            else:
                #same as Read N Characters Given read4, the first variation
                r=read4(buf4) #chars read
                if(r==0):
                    #no more chars to read from file! 
                    break
                for i in range(r):
                    self.queue.append(buf4[i]) #add the chars read to queue
                    
          
        return chars_read
