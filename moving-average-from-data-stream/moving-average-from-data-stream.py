class MovingAverage:

    def __init__(self, size: int):
        self.size= size
        self.queue=[]
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        total=sum(self.queue[-self.size:])

        return total/min(len(self.queue),self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)