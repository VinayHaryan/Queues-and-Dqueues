import collections
class RecentCounter:

    def __init__(self):
        self.q = collections.deque()
        

    def ping(t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
        



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)