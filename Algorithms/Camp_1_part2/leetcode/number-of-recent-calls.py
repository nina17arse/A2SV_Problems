class RecentCounter:
    def __init__(self):
        from collections import deque
        self.queue=deque()
        self.left=0

    def ping(self, t: int) -> int:
        while self.queue:
            if self.queue[0]>=t-3000:
                break
            self.queue.popleft()
            self.left-=1
        self.queue.append(t)
        self.left+=1
        return self.left
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)