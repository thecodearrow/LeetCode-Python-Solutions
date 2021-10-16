class HitCounter:
    def __init__(self):
        self.log=deque() #(timestamp,freq)

    def hit(self, timestamp: int) -> None:
        if(self.log and self.log[-1][0]==timestamp):
            #if many timestamps arrive at the same time, we increment freq
            self.log[-1][1]+=1 
        else:
            self.log.append([timestamp,1]) #init with freq 1
        

    def getHits(self, timestamp: int) -> int:
        
        while self.log and timestamp-self.log[0][0]>=300:
            self.log.popleft() #remove hits older than 5 mins, this also removes multiple hits with same timestamp at once! 
        
        count=0 #count of remaining hits
        for timestamp,freq in self.log:
            count+=freq
        return count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
