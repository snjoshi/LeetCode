class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        squeue=deque()
        tqueue=deque()
        
        for i in s:
            if i=='#':
                if squeue:
                    squeue.popleft()
            else:
                squeue.appendleft(i)
            
        for i in t:
            if i=='#':
                if tqueue:
                    tqueue.popleft()
            else:
                tqueue.appendleft(i)
        
        if squeue==tqueue:
            return True
        return False