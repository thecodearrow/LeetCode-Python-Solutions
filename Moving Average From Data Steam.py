class MovingAverage:
    def __init__(self, size: int):
        self.last_k=deque()
        self.window_sum=0
        self.window_size=size
        self.current_size=0
        

    def next(self, val: int) -> float:
        self.last_k.append(val)
        self.current_size=min(self.current_size+1,self.window_size)
        self.window_sum+=val
        if(len(self.last_k)>self.window_size):
            popped=self.last_k.popleft()
            self.window_sum-=popped
        avg=self.window_sum/self.current_size
        return avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
