class MovingAverage:
    
    def __init__(self, size: int):
        self.q=deque()
        self.size=size
        self.avg=0
        self.sum=0
        

    def next(self, val: int) -> float:
        pop =0
        if len(self.q) == self.size:
            pop = self.q.popleft()
            self.q.append(val)
        else:
            self.q.append(val)
        self.sum= self.sum -pop + val 
        self.avg =  self.sum/len(self.q)
        
        return self.avg
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)