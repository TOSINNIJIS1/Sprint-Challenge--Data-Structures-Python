class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.curr = 0

    def append(self, item):
        if len(self.storage) < self.capacity:            
            self.storage.append(item)  
        else:
            self.storage[self.curr] = item

        self.curr += 1

        if self.curr == self.capacity:
            self.curr = 0
    def get(self):
        return self.storage